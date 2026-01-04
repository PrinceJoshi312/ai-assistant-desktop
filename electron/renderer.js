const sendBtn = document.getElementById("sendBtn");
const input = document.getElementById("msg");
const chat = document.getElementById("chat");

function appendMessage(sender, text) {
  const msgDiv = document.createElement("div");
  msgDiv.style.padding = "8px";
  msgDiv.style.borderBottom = "1px solid #334155";
  msgDiv.innerHTML = `<b>${sender}:</b> ${text}`;
  chat.appendChild(msgDiv);
  chat.scrollTop = chat.scrollHeight;
}

async function handleSend() {
  const message = input.value.trim();
  if (!message) return;

  appendMessage("You", message);
  input.value = "";

  try {
    const data = await window.api.sendMessage(message);
    appendMessage("Bot", data.reply || "No response received.");
  } catch (error) {
    console.error("Fetch Error:", error);
    appendMessage("Bot", "Error: Backend is not responding. Is run.py running?");
  }
}

// Click to send
sendBtn.addEventListener("click", handleSend);

// Enter to send
input.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    handleSend();
  }
});