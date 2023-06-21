// whenever the site gets clicked
document.body.addEventListener('click', event => {
    
    const clicked_element = event.target;

    // --- load email page
    const like_buttons   = document.querySelectorAll(".like-button")
    like_buttons.forEach( (like_button) => {
      if (like_button === clicked_element) {
        console.log("hello");
      }
    });
});
