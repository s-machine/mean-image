function hexToValue(color){
  var r = parseInt(color.substr(1,2), 16); // Grab the hex representation of red (chars 1-2) and convert to decimal (base 10).
  var g = parseInt(color.substr(3,2), 16);
  var b = parseInt(color.substr(5,2), 16);
  
  r /= 255, g /= 255, b /= 255;
  var max = Math.max(r, g, b), min = Math.min(r, g, b);
  var h, s, l = (max + min) / 2;
  return l;
}