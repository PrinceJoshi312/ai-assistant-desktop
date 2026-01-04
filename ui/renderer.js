async function send() {
  const input = document.getElementById("msg");
  const chat = document.getElementById("chat");

  const res = await window.api.sendMessage(input.value);

  chat.textContent += `\nYou: ${input.value}`;
  chat.textContent += `\nBot: ${res.reply || "✔ Action executed"}`;

  input.value = "";
}
function toggleTheme() {
  document.body.classList.toggle("light");
}

async function send() {
  const input = document.getElementById("msg");
  const chat = document.getElementById("chat");
  const text = input.value.trim();
  if (!text) return;

  chat.innerHTML += `<p><b>You:</b> ${text}</p>`;
  input.value = "";

  try {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    });

    const data = await res.json();

    if (data.reply) {
      chat.innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;
    }

    if (data.action) {
      chat.innerHTML += `<p style="color:#38bdf8"><b>Action:</b> ${data.action.action}</p>`;
      console.log("Action payload:", data.action);
    }

    chat.scrollTop = chat.scrollHeight;

  } catch (err) {
    chat.innerHTML += `<p style="color:red">Backend not reachable</p>`;
  }
}
