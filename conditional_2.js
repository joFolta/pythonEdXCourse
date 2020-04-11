const x = 6;
const z = 1;
if (x > 5) {
  console.log("Greater than 5");
}
if (x == 6) {
  console.log("Since x is 6, run this code, too:");
  if (false) {
    console.log("false");
  } else if (z == 10000001) {
    console.log("z is 10000001.");
  } else {
    console.log("It was true.");
  }
}
