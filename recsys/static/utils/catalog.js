document.addEventListener('DOMContentLoaded', function() {

});

const buttons = document.querySelectorAll('.catalog-navbar button');
const contentBlocks = document.querySelectorAll('.content-block');

function switchContent(targetId) {

};

buttons.forEach(button => button.addEventListener('click', function(event) {

}));

document.addEventListener("DOMContentLoaded", () =>{

   const buttons = document.querySelectorAll(".catalog-navbar button");
   const contentBlocks = document.querySelectorAll(".content-block");

   function switchContent(targetId){
       contentBlocks.forEach(block => block.classList.remove("active"));

       const targetBlock = document.querySelector(`${targetId}`);
       if (targetBlock){
           targetBlock.classList.add("active");
       }
   }

   buttons.forEach(button =>{
      button.addEventListener("click", event =>{
         let targetId=button.getAttribute("data-target");
         switchContent(targetId);
      });
   
});
});