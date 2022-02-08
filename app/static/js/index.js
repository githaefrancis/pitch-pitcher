console.log("we just ran");

document.addEventListener('DOMContentLoaded',(event)=>{


  console.log("we ran after");

document.addEventListener('click',(e)=>{
  buttonVote=e.target
  nameOfNode=buttonVote.nodeName
  console.log(buttonVote.nodeValue)
  buttonCLickedName=buttonVote.getAttribute('Name')
  pitch_id=buttonVote.closest('div').getAttribute('id')
  console.log(buttonCLickedName)
  if (buttonVote.classList.contains('active') && nameOfNode=='I'){

    buttonVote.classList.remove('active')

    
  }
  else if(!buttonVote.classList.contains('active') && nameOfNode=='I'){
    buttonVote.classList.add('active')
    if(buttonCLickedName=='upvote'){
        location.href=`/pitch/${pitch_id}/upvote`
    }
    else if(buttonCLickedName=='downvote'){
      location.href=`/pitch/${pitch_id}/downvote`
       console.log('I am a downvote')
    }
    closestdiv=buttonVote.closest('div').getAttribute('id')
    console.log(closestdiv)
    // location.href='/gooo'
    // console.log(buttonVote.closest('[name=downvote]'))
    // if (buttonCLickedName=='upvote' && buttonVote.closest('i').classList.contains('active')){

    //   buttonVote.closest('.downvote').classList.remove('active');
    // }


  }
  // button.classList.add('bg-danger','text-white')
  console.log(e.target)
})

// document.addEventListener('click',(e)=>{
//   buttonUpvote=e.target
//   if (buttonUpvote.classList.contains('active')){
//     buttonUpvote.classList.remove('active')
//   }

//   else{

//     buttonUpvote.classList.add('active')
//   }
// })

})