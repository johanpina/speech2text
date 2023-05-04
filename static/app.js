const textButton = document.getElementById("textButton");
const audioButton = document.getElementById("audioButton");
const textFormContainer = document.getElementById("textFormContainer");
const audioFormContainer = document.getElementById("audioFormContainer");
const processTextButton = document.getElementById("process-text-button");
const processAudioButton = document.getElementById("process-audio-button");
const customAudioButton = document.getElementById("custom-audio-button");
const audioFileInput = document.getElementById("audio-file");

textButton.addEventListener("click", () => {
  textFormContainer.style.display = "block";
  audioFormContainer.style.display = "none";
});

audioButton.addEventListener("click", () => {
  textFormContainer.style.display = "none";
  audioFormContainer.style.display = "block";
});

processTextButton.addEventListener("click", async () => {
  const textInput = document.getElementById("text-input");
  const iaConclusionTitle = document.getElementById("ia-conclusion-title");
  const iaConclusion = document.getElementById("ia-conclusion");
  const loadingText = document.getElementById("loading-text");

  iaConclusionTitle.style.display = "none";
  iaConclusion.style.display = "none";
  loadingText.style.display = "block";

  const response = await fetch("/api/prompt_medico", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ texto: textInput.value }),
  });

  const data = await response.json();

  iaConclusionTitle.style.display = "block";
  iaConclusion.style.display = "block";
  iaConclusion.value = data.response;
  loadingText.style.display = "none";
});

customAudioButton.addEventListener("click", () => {
  audioFileInput.click();
});

audioFileInput.addEventListener("change", () => {
  customAudioButton.textContent = audioFileInput.files[0].name;
});

processAudioButton.addEventListener("click", async () => {
  const audioResponse = document.getElementById("audio-response");
  const loadingAudio = document.getElementById("loading-audio");
  const successAudio = document.getElementById("success-audio");

  const file = audioFileInput.files[0];
  const formData = new FormData();
  formData.append("uploaded_file", file);

  loadingAudio.style.display = "block";
  successAudio.style.display = "none";
  audioResponse.style.display = "none";

  const response = await fetch("/api/process_audio", {
    method: "POST",
    body: formData,
  });

  const data = await response.json();

  loadingAudio.style.display = "none";
  successAudio.style.display = "block";
  audioResponse.style.display = "block";
  audioResponse.value = data.texto;
});
