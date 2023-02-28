// ADD NEW VIDEO PAGE

// ADD VIDEO
const videoUploadContainer = document.getElementById("video-upload-container");
const videoUpload = document.getElementById("video-upload");
// const videoUploadButton = document.getElementById("video-upload-button");
const videoList = document.getElementById("video-list");

videoUpload.addEventListener("change", (e) => {
  updateVideoList();
});

videoUploadContainer.addEventListener("dragover", (e) => {
  e.preventDefault();
  e.stopPropagation();
  videoUploadContainer.classList.add("dragover");
});

videoUploadContainer.addEventListener("dragleave", (e) => {
  e.preventDefault();
  e.stopPropagation();
  videoUploadContainer.classList.remove("dragover");
});

videoUploadContainer.addEventListener("drop", (e) => {
  e.preventDefault();
  e.stopPropagation();
  videoUploadContainer.classList.remove("dragover");
  videoUpload.files = e.dataTransfer.files;
  updateVideoList();
});

// videoUploadButton.addEventListener("click", () => {
//   videoUpload.click();
// });

function updateVideoList(){
  videoList.innerHTML = "";
  for (let i = 0; i < videoUpload.files.length; i++) {
    const file = videoUpload.files[i];
    const li = document.createElement("li");
    li.innerHTML = file.name;
    videoList.appendChild(li);
  }
}


// ADD THUMBNAIL
const thumbnailUploadContainer = document.getElementById("thumbnail-upload-container");
const thumbnailUpload = document.getElementById("thumbnail-upload");
// const thumbnailUploadButton = document.getElementById("thumbnail-upload-button");
const thumbnailList = document.getElementById("thumbnail-list");

thumbnailUpload.addEventListener("change", (e) => {
  updateThumbnailList();
});

thumbnailUploadContainer.addEventListener("dragover", (e) => {
  e.preventDefault();
  e.stopPropagation();
  thumbnailUploadContainer.classList.add("dragover");
});

thumbnailUploadContainer.addEventListener("dragleave", (e) => {
  e.preventDefault();
  e.stopPropagation();
  thumbnailUploadContainer.classList.remove("dragover");
});

thumbnailUploadContainer.addEventListener("drop", (e) => {
  e.preventDefault();
  e.stopPropagation();
  thumbnailUploadContainer.classList.remove("dragover");
  thumbnailUpload.files = e.dataTransfer.files;
  updateThumbnailList();
});

// thumbnailUploadButton.addEventListener("click", () => {
//   thumbnailUpload.click();
// });

function updateThumbnailList(){
  thumbnailList.innerHTML = "";
  for (let i = 0; i < thumbnailUpload.files.length; i++) {
    const file = thumbnailUpload.files[i];
    const li = document.createElement("li");
    li.innerHTML = file.name;
    thumbnailList.appendChild(li);
  }
}