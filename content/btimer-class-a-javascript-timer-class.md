Title: BTimer Class: A Javascript Timer Class
Date: 2007-04-11 18:26
Category: all
Tags: javascript
Slug: btimer-class-a-javascript-timer-class

Note: I just found out this doesn't work in Internet Explorer. If you
happen to use Internet Explorer I'm sorry; I'm sorry that you haven't
been shown a better browser sooner. [Get Firefox.][]

In continuing my CS162 project I decided my previous timer wasn't all
that pimp since I needed to add a few attributes such as a pause/stop
method and a reset method. Using the previous single function method
somewhat worked for this but the number of arguments that needed to be
passed to the function grew rather quickly, and in addition I had to
make use of global variables. It was at this point I knew I needed to
move the timer into a class to make it more portable and thus I came up
with BTimer.

The BTimer Class allows one to run multiple Javascript timers without
having to worry about the details of the setTimeout function or
setInterval. This is particularly useful in cases where a page has
different AJAX portions that need to be updated at different rates.

~~~~ {lang="Javascript" line="1"}
// Bryce Boe
// http://www.bryceboe.com/2007/04/11/btimer-class-a-javascript-timer-class/
function BTimer(interval,f,args) {
    this.init(interval,f,args);
}
BTimer.prototype = {
    init:function(interval,f,args) {
        this.setUpdateFunction(f,args);
        this.setStartFunction(null,[]);
        this.setStopFunction(null,[]);
        this.setResetFunction(null,[]);
        this.running = false;
        this.ms = interval;
        this.count = 0;
        this.limit = Infinity;
    },
    _run:function() {
        if (!this.running) return;
        if (this.count>=this.limit) {
            this.stop();
            return;
        }
        this.count++;
        this.updateFunc.apply(null,this.updateArgs);
        var self=this;
        setTimeout(function(){self._run(self.ms);},this.ms);
    },
    start:function() {
        if (!this.running) {
            this.running = true;
            this._run();
            if (this.startFunc != null)
                this.startFunc.apply(null,this.startArgs);
        }
    },
    stop:function() {
        if (this.running) {
            this.running = false;
            if (this.stopFunc != null) this.stopFunc.apply(null,this.stopArgs);
        }
    },
    reset:function() {
        this.count = 0;
        if (this.resetFunc != null) this.resetFunc.apply(null,this.resetArgs);
    },
    setUpdateFunction:function(f,args) {
        this.updateFunc = f;
        this.updateArgs = args;
    },
    setStartFunction:function(f,args) {
        this.startFunc = f;
        this.startArgs = args;
    },
    setStopFunction:function(f,args) {
        this.stopFunc = f;
        this.stopArgs = args;
    },
    setResetFunction:function(f,args) {
        this.resetFunc = f;
        this.resetArgs = args;
    },
    setLimit:function(limit) {
        this.limit=limit;
    },
    setInterval:function(interval) {
        this.ms=interval;
    },
    getCount:function() {
        return this.count;
    }
}
~~~~

The init function is the constructor for the BTimer class and called
automatically when one writes: "new BTimer(someFunc,someList)". The
constructor takes as its first argument the update interval in
milliseconds, the name of the function to call on update and finally a
list of arguments that should be passed to the update function. If the
update function takes no arguments one must simply pass in an empty
array [].

The BTimer's \_run() function is where the magic occurs and should never
be called directly. This function verifies that it should be running and
if so it increments the count, calls the update function, and then
creates the timer loop. In the event we reached the run limit it calls
its stop function so that the optional user defined stop function may be
called.

The BTimer's start() function calls the optional user specified start
function, and then begins the timer by calling \_run(). It also checks
to see if it has already been started so that it doesn't initialize a
parallel setTimeout command.

The BTimer's stop() function stops the timer and calls the optional user
specified stop Function. The stop function acts like a tape player
rather than a cd player as on resume (calling start()) the counter
continues where it left off.

The BTimer's reset() function resets the count back to zero and
optionally calls the user defined reset function. Note that this does
not change the running status of the counter.

The setUpdateFunction, setStartFunction, setStopFunction and
setResetFunction all set their respective optional functions. Each take
the function to be called on the particular event and the arguments that
should be passed to that function as a list. Just like the constructor
if the function takes no arguments then an empty array [] needs to be
passed in as the second argument.

The setLimit function updates the timer limit. By default the timer
limit is the javascript value *Infinity*.

The setInterval function updates the wait time between the update
function calls. This can be called while the timer is running and will
take place after the event from the last setTimeout function occurs. An
example to demonstrate this is calling start on a one minute timer and
then immediately changing the interval to be 5 seconds. The 5 second
interval wont take place until the one minute timer has expired.

Finally the getCount() function returns the timer count.

To demonstrate BTimer in action check out the following:

<p>
<script type="text/javascript" src="/images/2007/04/btimer0.js"></script>
  
<textarea id="BTimerStatus0" style="width:200px;height:150px;">Status
Area</textarea>

</p>
<div id="BTimerDynamic0">
Count: 0

</div>
<input type="button" value="Start" id="BTimerStart0" onclick="BTimerMyStart0();"></input><input type="button" value="Pause" id="BTimerPause0" onclick="BTimerMyTimer0.stop();" disabled></input><input type="button" value="Reset" id="BTimerReset0" onclick="BTimerMyTimer0.reset();" disabled></input>  

<input type="radio" id="BTimerRadio00" name="BTimertimeout" onclick="BTimerMyTimer0.setInterval(300);BTimerOther0('selected .3 second');" checked disabled></input>
0.3 second  
<input type="radio" id="BTimerRadio10" name="BTimertimeout" onclick="BTimerMyTimer0.setInterval(1000);BTimerOther0('selected 1 second');" disabled></input>
1 second  
<input type="radio" id="BTimerRadio20" name="BTimertimeout" onclick="BTimerMyTimer0.setInterval(5000);BTimerOther0('selected 5 seconds');" disabled></input>
5 seconds  

Note: Clicking on reset does not update the count to 0.

The extra needed javascript functions for this are the following:

~~~~ {lang="Javascript" line="1"}
function BTimerMyStart0() {
    document.getElementById('BTimerPause0').disabled=false;
    document.getElementById('BTimerReset0').disabled=false;
    document.getElementById('BTimerStart0').disabled=true;
    document.getElementById('BTimerRadio00').disabled=false;
    document.getElementById('BTimerRadio10').disabled=false;
    document.getElementById('BTimerRadio20').disabled=false;
    if (typeof BTimerMyTimer0 == 'undefined') {
        BTimerMyTimer0 = new BTimer(300,BTimerMyUpdate0,[]);
        BTimerMyTimer0.setLimit(50);
        BTimerMyTimer0.setStopFunction(BTimerMyPause0,[]);
        BTimerMyTimer0.setResetFunction(BTimerOther0,['called reset']);
        BTimerMyTimer0.setStartFunction(BTimerOther0,['called start']);
    }
    BTimerMyTimer0.start();
}
function BTimerMyUpdate0() {
    document.getElementById('BTimerDynamic0').innerHTML="Count: "
        +BTimerMyTimer0.count;
}
function BTimerMyPause0() {
    document.getElementById('BTimerStart0').disabled=false;
    document.getElementById('BTimerPause0').disabled=true;
    BTimerOther0('called pause');
}
function BTimerOther0(string) {
    if (typeof BTimerMyStatusCount0 == 'undefined') BTimerMyStatusCount0 = 0;
    document.getElementById('BTimerStatus0').innerHTML = BTimerMyStatusCount0++
        +": " + string + "\n"
        + document.getElementById('BTimerStatus0').innerHTML;
}
~~~~

And the accompanying html:

~~~~ {lang="html4strict"}
Status Area
Count: 0




 0.3 second
 1 second
 5 seconds
~~~~

This javascript code is fairly self explanatory with the exception of
BTimerMyStart0. Since I want to create my timer the first time I call
start it is necessary to verify that upon further start button presses
the same does not occur. This is what line 8 does. One can also see that
I set the limit to 50 in addition to setting start, stop and reset
functions. Just a reminder that these functions are purely optional; I'm
using them to demonstrate their purpose.

Once the start function is called we now have a variable BTimerMyTimer0
which points to our timer object. We interact with this object by
defining our onclick actions with the pause and reset buttons.

Finally the BTimerOther0 function simply updates the textarea with the
string it receives. This function demonstrates passing arguments to a
user defined event function.

Well I think that's it, feel free to use BTimer.js but please keep the
two lines of comments so that one may have access to this post for
support on the timer.

[BTimer Class Source][]

  [Get Firefox.]: http://www.getfirefox.com
  [BTimer Class Source]: /images/2007/04/btimer.js
    "BTimer Class"
