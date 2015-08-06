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
