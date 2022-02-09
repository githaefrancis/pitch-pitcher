
// document.addEventListener("DOMContentLoaded", (event) => {
  $(()=>{

  document.addEventListener("click", (e) => {
    buttonVote = e.target;
    nameOfNode = buttonVote.nodeName;
  
    buttonCLickedName = buttonVote.getAttribute("Name");
    pitch_id = buttonVote.closest("div").getAttribute("id");
    
    if (
      (buttonVote.classList.contains("upvote") ||
        buttonVote.classList.contains("downvote")) &&
      nameOfNode == "I"
    ) {
      if (buttonCLickedName == "upvote") {
        location.href = `/pitch/${pitch_id}/upvote`;
      } else if (buttonCLickedName == "downvote") {
        location.href = `/pitch/${pitch_id}/downvote`;
        
      }
    }
  });

setTimeout(function() {
    $('.flashes').fadeOut('fast');
}, 10000);

})
// });
