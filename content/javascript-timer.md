Title: JavaScript Timer
Date: 2007-04-06 01:03
Category: all
Tags: javascript
Slug: javascript-timer

For my CS162 class we have to do a project requiring some AJAX. I've actually
never used AJAX before, and really haven't used javascript other than to
manipulate already existing html information. However despite my inexperience
with javascript I found this function to be pretty robust and perhaps helpful
to many others. Anyways I found myself needing a javascript wait function which
isn't available and thus I came across a few solutions. The main way appears to
be making use of the setTimeout function and use recursion to repeatedly call
the current function. I personally see problems with this method however since
people using a web browser don't need updates every millisecond it's fairly
safe to assume the javascript stack wont grow to the point where it's
suffocating memory.

Update: After writing this I realized I was wrong about recursion and the
setTimeout function. Thus this method really doesn't have any flaws. Though for
a more advanced timer please see my next post.

Please note that with all my sample scripts from this point on I require that
my name and website be retained in the event of using the code. If you wish to
use without my information please email me.

First the code for those that just want to use it:

    // Bryce Boe
    // Originally posted: http://www.bryceboe.com/2007/04/06/javascript-timer/
    //
    // This is a pimp ass update function. It takes in
    // an interval in milliseconds, a count, a function name
    // and any number of arguments to pass to that function.
    // In this sense it should work with any function that
    // needs to be called at a specified interval.
    // The count specifies how many times to repeat. Any
    // negative value specifies to repeat forever.
    function timer(interval,count,someFunction) {
        args = [];
        for (i=3;i 0) tCount = count-1;
        else tCount = -1;
        command='timer('+interval+','+tCount+','+someFunction+',';
        for (i=3;i
    Now what does this do? This function allows you to call any other function at a specified interval, and the key part is that the function you are calling can have any number of any type of arguments and still be passed through this function. This works by passing the function as an argument to another function in javascript.
    Myself being a big python fan I was somewhat disappointed as the **kw functionality wasn't easily available but in looking at line 13 one can see how I implemented this. This uses the javascript arguments array to get the undeclared parameters which are then passed into the function we wish to call by using the javascript apply function. This is essentially a trick because apply is used so that we can pass an array as the arguments to the function rather than using apply to modify the meaning of the keyword this in the callee as I understand apply is really used for.
    Lines 17-24 recreate the same call we used to get into the timer function with the counter decremented by one if it is positive. Perhaps there is a better way to do this however this works as we need to have a string to pass to the setTimeout function. Also note on lines 19 and 20 I handled a special case for a string as an argument because otherwise the string will be evaluated rather before being passed. For other object types this may also need to be done to work properly.
    A very simple demonstration of this script is a counter function that has a min value, max value, step size and default starting location. In my example I use -25 as the min, 25 as the max -25 as the default start and .5 as the step size with a time interval of .3 seconds. By entering in a value in the text field before running the start point can be adjusted.



    Here is the code of the timer function:

    function myCounter(min,max,start,step,id) {
        curr = parseFloat(document.getElementById(id).value);
        if (isNaN(curr)) curr = start
        n = curr+step;
        if (min <= n && n <= max) {
            document.getElementById(id).value=n;
        }
    }

And the code used to start the timer:

Notice how I wrote the function to be passed the field which I wish to modify.
This easily allows for more robustness as I can easily change my timer function
to update any other html entity with a value field. With a bit more trickery
this function could take another argument which will allow it to modify the
innerHTML field if the element specified by the id doesn't have a value,
however I'll leave that up to you to figure out.

> One flaw I noticed while testing this post is that each time the start button
> is clicked a new timer is started thus making the counter go much faster.
> Feel free to correct that if needed, but it shouldn't be a problem if you're
> sure the timer will only be started once.

I think that's it, feel free to email me, or comment with any questions you may
have regarding this.
