// ADD PRODUCT PAGE
const fileUploadContainer = document.getElementById("file-upload-container");
const fileUpload = document.getElementById("file-upload");
const fileUploadButton = document.getElementById("file-upload-button");
const fileList = document.getElementById("file-list");

fileUpload.addEventListener("change", (e) => {
  updateFileList();
});

fileUploadContainer.addEventListener("dragover", (e) => {
  e.preventDefault();
  e.stopPropagation();
  fileUploadContainer.classList.add("dragover");
});

fileUploadContainer.addEventListener("dragleave", (e) => {
  e.preventDefault();
  e.stopPropagation();
  fileUploadContainer.classList.remove("dragover");
});

fileUploadContainer.addEventListener("drop", (e) => {
  e.preventDefault();
  e.stopPropagation();
  fileUploadContainer.classList.remove("dragover");
  fileUpload.files = e.dataTransfer.files;
  updateFileList();
});

function updateFileList(){
  fileList.innerHTML = "";
  for (let i = 0; i < fileUpload.files.length; i++) {
    const file = fileUpload.files[i];
    const li = document.createElement("li");
    li.innerHTML = file.name;
    fileList.appendChild(li);
  }
}