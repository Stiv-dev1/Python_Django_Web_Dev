const btnScroll = document.querySelector("#btnTop")

window.addEventListener("scroll", scrollFunction );

function scrollFunction(){
    if (window.pageYOffset > 300 ){
        if(!btnScroll.classList.contains("btnEntrance")){
          btnScroll.classList.remove("btnExit");
          btnScroll.classList.add("btnEntrance");
          btnScroll.style.display = "block";
       }
    }
    else{
        if(btnScroll.classList.contains("btnEntrance")) {
           btnScroll.classList.remove("btnEntrance");
           btnScroll.classList.add("btnExit");
           setTimeout(function() {
           btnScroll.style.display = "none";
      }, 250);
    }
  }
}


btnScroll.addEventListener("click", backToTop);
function backToTop(){
  const targetPosition = 0;
  const startPosition = window.pageYOffset;
  const distance = targetPosition - startPosition;
  const duration = 750;
  let start = null;

  window.requestAnimationFrame(step);

  function step(timestamp) {
    if (!start) start = timestamp;
    const progress = timestamp - start;
    window.scrollTo(0, easeInOutCubic(progress, startPosition, distance, duration));
    if (progress < duration) window.requestAnimationFrame(step);
  }
}

function easeInOutCubic(t, b, c, d) {
	t /= d/2;
	if (t < 1) return c/2*t*t*t + b;
	t -= 2;
	return c/2*(t*t*t + 2) + b;
};



const closesidebar = document.querySelector("#toggle-close")
closesidebar.addEventListener("click", toggleclose() );
function toggleclose() {
    document.querySelector(".sidebar").style.width="0";
    document.querySelector(".sidebar").style.display="none";
    document.querySelector("#togglebtn").style.display="block";
    document.querySelector(".main-content").style.marginLeft="40px";


}

const tag = document.querySelector("#togglebtn")

tag.addEventListener("click", sidebar())
function sidebar() {
   document.querySelector(".sidebar").style.display="block";
     document.querySelector(".sidebar").style.width="280px";
         document.querySelector("#togglebtn").style.display="none";


}
function sizing(mq){
   if( mq.matches ){
     document.querySelector(".sidebar").style.width="0";
     document.querySelector(".sidebar").style.display="none";
     document.querySelector("#togglebtn").style.display="block";
     document.querySelector(".main-content").style.marginLeft="40px";
    }
    else {
       document.querySelector(".sidebar").style.display="block";
       document.querySelector(".sidebar").style.width="280px";
       document.querySelector("#togglebtn").style.display="none";

}
    }
 var mq = window.matchMedia('(max-width: 600px)');
 sizing(mq)
 mq.addEventListener("change", sizing)


