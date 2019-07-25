// code for the cookie clicker!
// DawgBytes 2018: Web Design class - A glimpse of Javascript.
// This may be REALLY difficult.
// ***********IF YOU NEED HELP, ASK THE COUNSELORS :D************* //

//************* NOTHING TO DO HERE :) *************//
// state of the game!
// this is where we keep track of the user's score.
//	I already made these for you :) so, don't touch the next 4 lines.
// we set all of these variables to 0, since in the beginning of the game,
//	we start with 0 apples, 0 oranges, no points, and 0 points per second.
var appleCount = 0; // the total number of apple the player has.
var orangeCount = 0; // total number of oranges the player has
var durianCount = 0; // total number of durians the player has
var farmerCount = 0; // total number of farmers the player has
var cityCount = 0; // total number of cities the player has
var point = 0; // total points the player has
var perSec = 0; // the amount of points the player gets per second based on appleCount and orangeCount

// when the Get Cookie! button is clicked, this function is executed.
//	This function is already made for you!
//	Read the description to see what I did.
function getCookie() {
  // when the user gets a cookie, we increase the point by 1.
  point += 1;
  // then we update the website to display the score!
  update();
}

//************* HELLO!!! LOOK AT THE NEXT LINE!!! *************//
//************* BELOW IS WHERE YOU GET TO CODE :D *************//

// This function is executed when the Buy Apple button is clicked.
// Here is what you need to do:
//	- ONLY let the user buy an apple IF the user has at least 20 points.
//			(otherwise, they would be cheating... and cheating is bad!)
//  - If the player has enough points, let them buy it by
//			- increasing the appleCount by 1
//			AND
//			- subtracting 20 points from the amount of point the player has.
//	- Don't forget to update the website's display.
function buyApple() {
  if (/* replace this comment with a boolean expression to check that the user has enough points */) {
    appleCount += /* replace this comment with the correct amount of apple to add to appleCount, this should be simple */;
    point -= /* replace this comment with the correct price of the apple. */;
    calculatePerSecond(); // since the per second is different now, we recalculate persecond. Nothing to do here.
    update() // we update the website with correct information about the state of the game. Nothing to do here.
  }
}

// This function is executed when the Buy Orange button is clicked.
// Here is what you need to do:
//	- ONLY let the user buy an orange IF the user has at least 100 points.
//			(otherwise, they would be cheating... and cheating is bad!)
//  - If the player has enough points, let them buy it by
//			- increasing the orangeCount by 1
//			AND
//			- subtracting 100 points from the amount of point the player has.
//	- Don't forget to update the website's display.
function buyOrange() {
  // This time, you are going to do most of the coding.
  // 	It shoud be pretty similar to the buyApple() function.
  //	Good luck!
}

// this function calculates how many points the player should get per second.
// This involves some math. Do your best to finish! Good luck!
function calculatePerSecond() {
  perSec = /* Replace this with the correct mathematical expression */;
}

// This function is called every second to simulate getting perSec amount of points each second.
// Nothing to do here :) Just wanted you to see how updating the points work!
//	This part is easy, so I decided not to make you code this one.
function calculatePoints() {
  point += perSec;
  update();
}


// This function is executed when the Buy Durian button is clicked.
// Here is what you need to do:
//	- ONLY let the user buy a durian IF the user has at least 1000 points.
//			(otherwise, they would be cheating... and cheating is bad!)
//  - If the player has enough points, let them buy it by
//			- increasing the durianCount by 1
//			AND
//			- subtracting 1000 points from the amount of point the player has.
//	- Don't forget to update the website's display.
function buyDurian() {
  // This time, you are going to do most of the coding.
  // 	It shoud be pretty similar to the buyApple() function.
  //	Good luck!
}

// This function is executed when the Buy Farmer button is clicked.
// Here is what you need to do:
//	- ONLY let the user buy an Farmer IF the user has at least 10000 points.
//			(otherwise, they would be cheating... and cheating is bad!)
//  - If the player has enough points, let them buy it by
//			- increasing the farmerCount by 1
//			AND
//			- subtracting 10000 points from the amount of point the player has.
//	- Don't forget to update the website's display.
function buyFarmer() {
  // This time, you are going to do most of the coding.
  // 	It shoud be pretty similar to the buyApple() function.
  //	Good luck!
}

// This function is executed when the Buy City button is clicked.
// Here is what you need to do:
//	- ONLY let the user buy an City IF the user has at least 100 points.
//			(otherwise, they would be cheating... and cheating is bad!)
//  - If the player has enough points, let them buy it by
//			- increasing the cityCount by 1
//			AND
//			- subtracting 1000000 points from the amount of point the player has.
//	- Don't forget to update the website's display.
function buyCity() {
  // This time, you are going to do most of the coding.
  // 	It shoud be pretty similar to the buyApple() function.
  //	Good luck!
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
