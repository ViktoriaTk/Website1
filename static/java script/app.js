/*const inputs=document.querySelectorAll(".input-container");

function focusFunc() {
    let parent=this.parentNode;
    parent.classList.add("focus");
}

function blurFunc() {
    let parent=this.parentNode;
    if(this.value==""){
      parent.classList.remove("focus");   
    }
   
}

inputs.forEach((input-container) => {
    input-container.addEventListener("focus", focusFunc);
    input-container.addEventListener("blur", blurFunc);

});*/

//CONTACT FORM
const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});


// HIDE/APPEAR 
/*
function toggle() {
  var x = document.getElementById("div1");

  if(x.style.display==="none") {
    x.style.display = "block";
  }

  else {
    x.style.display==="none";
  }
}
*/