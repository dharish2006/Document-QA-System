import { useState } from "react";

function ChatInput({ onSend, loading }) {
    const [question, setQuestion] = useState("");

    const handleSend = () => {
        if (!question.trim()) return;

        onSend(question);
        setQuestion("");
    };

    const handleKeyDown = (e) => {
        if (e.key === "Enter") {
            handleSend();
        }
    };

    return (
        <div className="border-t bg-white p-4">
            <div className="flex gap-3">
                <input
                    type="text"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    onKeyDown={handleKeyDown}
                    placeholder="Ask anything about the uploaded document..."
                    className="flex-1 border rounded-lg px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500"
                    disabled={loading}
                />

                <button
                    onClick={handleSend}
                    disabled={loading}
                    className="bg-blue-600 hover:bg-blue-700 text-white px-6 rounded-lg disabled:bg-gray-400"
                >
                    Send
                </button>
            </div>
        </div>
    );
}

export default ChatInput;