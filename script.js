const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatBox = document.getElementById("chat-box");


function addMessage(message, sender) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add(
        "message",
        sender === "user"
            ? "user-message"
            : "bot-message"
    );


    if (sender === "user") {

        messageDiv.innerHTML = `
            <div class="message-content">
                <strong>You</strong>
                <p>${escapeHTML(message)}</p>
            </div>

            <div class="avatar">
                👤
            </div>
        `;

    } else {

        messageDiv.innerHTML = `
            <div class="avatar">
                🤖
            </div>

            <div class="message-content">
                <strong>AI Assistant</strong>
                <p>${escapeHTML(message)}</p>
            </div>
        `;
    }


    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


function escapeHTML(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}


async function sendMessage() {

    const message = messageInput.value.trim();

    if (!message) {
        return;
    }


    // Display user message
    addMessage(message, "user");

    messageInput.value = "";

    sendButton.disabled = true;

    sendButton.textContent = "Sending...";


    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();


        if (data.success) {

            addMessage(data.response, "bot");

        } else {

            addMessage(
                "Something went wrong. Please try again.",
                "bot"
            );

        }

    } catch (error) {

        addMessage(
            "Unable to connect to the server. Please try again.",
            "bot"
        );

        console.error(error);

    }


    sendButton.disabled = false;

    sendButton.textContent = "Send";

    messageInput.focus();
}


function sendSuggestion(message) {

    messageInput.value = message;

    sendMessage();
}


sendButton.addEventListener(
    "click",
    sendMessage
);


messageInput.addEventListener(
    "keypress",
    function(event) {

        if (event.key === "Enter") {

            sendMessage();

        }

    }
);
