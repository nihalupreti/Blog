const bookmarkIcon = document.querySelector(".ph");
let isBookmarked = false;

bookmarkIcon.addEventListener("click", () => {
  if (!isBookmarked) {
    bookmarkIcon.classList.remove("ph");
    bookmarkIcon.classList.add("lc");
    const pathElement = document.querySelector("path");
    pathElement.setAttribute(
      "d",
      "M7.5 3.75a2 2 0 0 0-2 2v14a.5.5 0 0 0 .8.4l5.7-4.4 5.7 4.4a.5.5 0 0 0 .8-.4v-14a2 2 0 0 0-2-2h-9z"
    );
    isBookmarked = true;
  } else {
    bookmarkIcon.classList.remove("lc");
    bookmarkIcon.classList.add("ph");
    const pathElement = document.querySelector("path");
    pathElement.setAttribute(
      "d",
      "M17.5 1.25a.5.5 0 0 1 1 0v2.5H21a.5.5 0 0 1 0 1h-2.5v2.5a.5.5 0 0 1-1 0v-2.5H15a.5.5 0 0 1 0-1h2.5v-2.5a.5.5 0 0 1 1 0z"
    );
    isBookmarked = false;
  }

  $(document).ready(function () {
    $(".ph").on("click", function () {
      const postId = $(this).data("post-id");
      console.log("Clicked on bookmark for post ID:", postId);
      $.ajax({
        url: "/bookmark",
        method: "POST",
        data: { postId: postId, bookmarked: isBookmarked ? "true" : "false" },
        success: function (response) {
          console.log("Bookmark posted to the server");
          console.log(response);
        },
        error: function (error) {
          console.error("Error posting bookmark to the server", error);
        },
      });
    });
  });
});
