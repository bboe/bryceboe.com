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
	document.getElementById('BTimerDynamic0').innerHTML="Count: "+BTimerMyTimer0.count;
}
function BTimerMyPause0() {
	document.getElementById('BTimerStart0').disabled=false;
	document.getElementById('BTimerPause0').disabled=true;
	BTimerOther0('called pause');
}
function BTimerOther0(string) {
	if (typeof BTimerMyStatusCount0 == 'undefined') BTimerMyStatusCount0 = 0;
	document.getElementById('BTimerStatus0').innerHTML = BTimerMyStatusCount0++ +": " + string + "\n" + document.getElementById('BTimerStatus0').innerHTML;
}


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
		self=this;
		setTimeout(function(){self._run(self.ms);},this.ms);
	},
	start:function() {
		if (!this.running) {
			this.running = true;
			this._run();
			if (this.startFunc != null) this.startFunc.apply(null,this.startArgs);
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
