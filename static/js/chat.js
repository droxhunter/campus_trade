const chatInput = document.getElementById('chatInput');
const chatButton = document.getElementById('sendMessage');
const chatMessages = document.getElementById('chatMessages');

chatButton.addEventListener('click', () => {
    const message = chatInput.value.trim();
    if (message) {
        // Add message to chatMessages
        const newMessage = document.createElement('div');
        newMessage.textContent = `You: ${message}`;
        chatMessages.appendChild(newMessage);

        // Simulate sending the message to the server
        chatInput.value = '';
    }
});
