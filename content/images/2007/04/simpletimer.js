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
	for (i=3;i<arguments.length;i++) args[i-3]=arguments[i];
	someFunction.apply(this,args);
	if (count > 0) tCount = count-1;
	else tCount = -1;
	command='timer('+interval+','+tCount+','+someFunction+',';
	for (i=3;i<arguments.length;i++) {
		if (typeof arguments[i]=='string')
			command+='\''+arguments[i]+'\'';
		else command+=arguments[i];
		if(i+1<arguments.length) command+=',';
	}
	command+=')';
	if (tCount != 0) setTimeout(command,interval);
}

function myCounter(min,max,start,step,id) {
	curr = parseFloat(document.getElementById(id).value);
	if (isNaN(curr)) curr = start
	n = curr+step;
	if (min <= n && n <= max) {
		document.getElementById(id).value=n;
	}
}
