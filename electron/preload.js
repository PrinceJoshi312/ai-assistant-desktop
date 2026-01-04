const { contextBridge } = require("electron");

console.log("✅ Preload script loaded");

async function waitForBackend() {
  for (let i = 0; i < 15; i++) {
    try {
      await fetch("http://127.0.0.1:8000/");
      return;
    } catch {
      await new Promise(r => setTimeout(r, 1000));
    }
  }
  throw new Error("Backend not responding");
}

contextBridge.exposeInMainWorld("api", {
  sendMessage: async (msg) => {
    await waitForBackend();

    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg })
    });

    if (!response.ok) {
      throw new Error("Backend error");
    }

    return response.json();
  }
});
