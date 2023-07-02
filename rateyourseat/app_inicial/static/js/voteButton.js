document.addEventListener('DOMContentLoaded', function() {
    const upvoteButton = document.querySelector('.upvote-button');
    const downvoteButton = document.querySelector('.downvote-button');

    upvoteButton.addEventListener('click', function() {
      this.classList.add('clicked');
      downvoteButton.classList.remove('clicked');
    });

    downvoteButton.addEventListener('click', function() {
      this.classList.add('clicked');
      upvoteButton.classList.remove('clicked');
    });
});