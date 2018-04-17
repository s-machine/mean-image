var screenTop = $(document).scrollTop();
var currentPageID = Math.floor(screenTop/$(window).height());

document.addEventListener('keydown', function(event)){
  if (event.keyCode == 38 && currentPageID > 1){
    console.log(currentPageID);
    window.location = "#" + toString(currentPageID-1);
  }
  else if (event.keyCode == 40 && currentPageID < 8){
    window.location = "#" + toString(currentPageID+1);  
    console.log(currentPageID);
  }
};