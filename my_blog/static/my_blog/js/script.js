const bookmarkIcons = document.querySelectorAll(".bookmark-button");
let isBookmarked = {};

bookmarkIcons.forEach((bookmarkIcon) => {
  const postId = bookmarkIcon.getAttribute("data-post-id");
  isBookmarked[postId] = false;

  bookmarkIcon.addEventListener("click", () => {
    if (!isBookmarked[postId]) {
      bookmarkIcon.classList.remove("ph");
      bookmarkIcon.classList.add("lc");
      const pathElement = bookmarkIcon.querySelector("path");
      pathElement.setAttribute(
        "d",
        "M7.5 3.75a2 2 0 0 0-2 2v14a.5.5 0 0 0 .8.4l5.7-4.4 5.7 4.4a.5.5 0 0 0 .8-.4v-14a2 2 0 0 0-2-2h-9z"
      );
      isBookmarked[postId] = true;
    } else {
      bookmarkIcon.classList.remove("lc");
      bookmarkIcon.classList.add("ph");
      const pathElement = bookmarkIcon.querySelector("path");
      pathElement.setAttribute(
        "d",
        "M17.5 1.25a.5.5 0 0 1 1 0v2.5H21a.5.5 0 0 1 0 1h-2.5v2.5a.5.5 0 0 1-1 0v-2.5H15a.5.5 0 0 1 0-1h2.5v-2.5zm-11 4.5a1 1 0 0 1 1-1H11a.5.5 0 0 0 0-1H7.5a2 2 0 0 0-2 2v14a.5.5 0 0 0 .8.4l5.7-4.4 5.7 4.4a.5.5 0 0 0 .8-.4v-8.5a.5.5 0 0 0-1 0v7.48l-5.2-4a.5.5 0 0 0-.6 0l-5.2 4V5.75z"
      );
      isBookmarked[postId] = false;
    }

    let favouritePosts = [];
    for (let i in isBookmarked) {
      if (isBookmarked[i]) {
        favouritePosts.push(i);
      }
    }

    console.log("final piece", favouritePosts);
    $.ajax({
      url: "/bookmark",
      method: "POST",
      data: {
        bookmarkedPosts: favouritePosts,
      },
      success: function (response) {
        console.log(response);
      },
      error: function (error) {
        console.error("Error posting bookmark to the server", error);
      },
    });
  });
});
