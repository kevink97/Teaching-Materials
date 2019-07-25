// state of the game!
// this is where we keep track of the user's score.

//	I already made these for you :) so, don't touch the next 4 lines.
var appleCount = 0;
var orangeCount = 0;
var durianCount = 0; // total number of durians the player has
var farmerCount = 0; // total number of farmers the player has
var cityCount = 0; // total number of cities the player has

var point = 0;
var perSec = 0;

function getCookie() {
  point += 1;
  update();
}

function buyApple() {
  if (point >= 20) {
    appleCount += 1;
    point -= 20;
    calculatePerSecond();
    update();
  }
}

function buyOrange() {
  if (point >= 100) {
    orangeCount += 1;
    point -= 100;
    calculatePerSecond();
    update();
  }
}

function calculatePerSecond() {
  perSec = appleCount * 1 + orangeCount * 5 + durianCount * 8 + farmerCount * 10 + cityCount * 20;
}

function calculatePoints() {
  point += perSec;
  update();
}

function buyDurian() {
  if (point >= 1000) {
    durianCount += 1;
    point -= 1000;
    calculatePerSecond();
    update();
  }
}

function buyFarmer() {
  if (point >= 10000) {
    farmerCount += 1;
    point -= 10000;
    calculatePerSecond();
    update();
  }
}

function buyCity() {
  if (point >= 1000000) {
    cityCount += 1;
    point -= 1000000;
    calculatePerSecond();
    update();
  }
}

//***************************************************//
// DON'T WORRY ABOUT ANYTHING BELOW THIS!
//	IF YOU WANT TO KNOW WHAT THE CODE DOES, LET COUNSELORS KNOW!
// NOTE:
//	IF FOR SOME REASON YOU WANT TO ADD MORE ITEMS
//		TO THE COOKIE CLICKER, LET ME KNOW.
//		IT'S NOT TOO COMPLICATED...BUT YOU WILL
//		NEED TO LEARN A BIT OF EXTRA CODE.

// pre-saves all updatable item on html.
var ps = document.getElementById("ps");
var ac = document.getElementById("ac");
var oc = document.getElementById("oc");
var du = document.getElementById("du");
var fa = document.getElementById("fa");
var ci = document.getElementById("ci");
var pt = document.getElementById("pt");

// updates each of the updatable items
//	based on current state.
function update() {
  ac.innerHTML = appleCount;
  oc.innerHTML = orangeCount;
  du.innerHTML = durianCount;
  fa.innerHTML = farmerCount;
  ci.innerHTML = cityCount;

  pt.innerHTML = point;
  ps.innerHTML = perSec;
}

// recalculate points every second.
//	this simulates the point/sec gain.
setInterval(calculatePoints, 1000);
//***************************************************//
