Title: Amazon S3: Convert Objects to Reduced Redundancy Storage
Date: 2010-07-02 13:37
Category: all
Tags: python, s3
Slug: amazon-s3-convert-objects-to-reduced-redundancy-storage

<ins datetime="2010-08-27T16:58:26+00:00">
**Edit 2010/08/27**: I thought I should update this page stating that the AWS
S3 Console was updated [about a month ago][] with a feature to convert entire
folders to/from Reduced Redundancy. Additionally the boto source has moved to
GIT, thus a few changes are needed to run my script of the latest tree, however
with the modification to the below checkout line it will still work from
SVN.</ins>

If you are like me, you are pleased by the fact that amazon made it even
cheaper to store information in Amazon S3 through their [reduced redundancy
storage model][]. Unfortunately until just [recently][] there wasn't a simple
way to convert your old objects to use the reduced redundancy storage model.
Using a new revision of [boto][], the python amazon aws package, I wrote a
script (derived from [one by the boto author][]) that will automatically
convert all your old objects in a bucket to use the reduced redundancy storage
model.

The script, shown at the bottom, currently requires a svn version of boto with
revision of at least 1595. Assuming you have python and subversion installed,
the following will get you up and running with the script, which can be
downloaded [here][]. Running the script concurrent times will take
significantly much less time, therefore stopping the script midway through is
of minor consequence.

`svn checkout http://boto.googlecode.com/svn/trunk/@1595 boto-read-only cd boto-read-only (as root) python setup.py install cd .. rm -rf boto-read-only ./convert_to_rss.py your_bucket_name [aws_access_key_id aws_secret_access_key]`

Note that you may alternatively put your aws\_access\_key\_id and
aws\_secret\_access\_key into the environment variables AWS\_ACCESS\_KEY\_ID
and AWS\_SECRET\_ACCESS\_KEY respectively.

    #!/usr/bin/env python
    import os, sys

    try:
        import boto.s3
        boto.s3.key.Key.change_storage_class
    except ImportError, e:
        sys.stderr.write('Package boto (svn rev. >= 1595) must be installed.\n')
        sys.exit(1)
    except AttributeError, e:
        sys.stderr.write('Invalid version of boto. Required svn rev. >= 1595.\n')
        sys.exit(1)

    def convert(bucket_name, aws_id, aws_key):
        s3 = boto.connect_s3(aws_id, aws_key)
        bucket = s3.lookup(bucket_name)
        if not bucket:
            sys.stderr.write('Invalid authentication, or bucketname. Try again.\n')
            sys.exit(1)
        print 'Found bucket: %s' % bucket_name
        sys.stdout.write('Converting: ')
        sys.stdout.flush()
        found = converted = 0
        try:
            for key in bucket.list():
                found += 1
                if key.storage_class != 'REDUCED_REDUNDANCY':
                    key.change_storage_class('REDUCED_REDUNDANCY')
                    converted += 1
                if found % 100 == 0:
                    sys.stdout.write('.')
                    sys.stdout.flush()
        except KeyboardInterrupt: pass

        print '\nConverted %d items out of %d to reduced redundancy storage.' %   
           (converted, found)

    def main():
        def usage(msg=None):
            if msg:
                sys.stderr.write('\n%s\n\n' % msg)
            sys.stderr.write(''.join(['Usage: %s bucket [aws_access_key_id ',
                                      'aws_secret_access_key]\n']) % sys.argv[0])
            sys.exit(1)

        if len(sys.argv) == 2:
            bucket = sys.argv[1]
            msg = ''
            if 'AWS_ACCESS_KEY_ID' in os.environ:
                aws_id = os.environ['AWS_ACCESS_KEY_ID']
            else:
                msg += 'Environment does not contain AWS_ACCESS_KEY_ID.\n'
            if 'AWS_SECRET_ACCESS_KEY' in os.environ:
                aws_key = os.environ['AWS_SECRET_ACCESS_KEY']
            else:
                msg += 'Environment does not contain AWS_SECRET_ACCESS_KEY.\n'
            if msg:
                usage(msg + 'Please set values in environment or pass them in.')
        elif len(sys.argv) == 4:
            bucket = sys.argv[1]
            aws_id = sys.argv[2]
            aws_key = sys.argv[3]
        else:
            usage()

        convert(bucket, aws_id, aws_key)

    if __name__ == '__main__':
        main()

  [about a month ago]: http://aws.amazon.com/about-aws/whats-new/2010/07/14/s3-announces-enhanced-support-reduced-redundancy-storage/
  [reduced redundancy storage model]: http://aws.amazon.com/about-aws/whats-new/2010/05/19/announcing-amazon-s3-reduced-redundancy-storage/
  [recently]: http://code.google.com/p/boto/source/detail?r=1595
  [boto]: http://code.google.com/p/boto/
  [one by the boto author]: http://www.elastician.com/2010/06/using-reduced-redundancy-storage-rrs-in.html
  [here]: /images/2010/07/convert_to_rrs.py
