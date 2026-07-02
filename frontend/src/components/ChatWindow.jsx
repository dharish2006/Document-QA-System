import Message from "./Message";
import LoadingSpinner from "./LoadingSpinner";

function ChatWindow({ messages, loading }) {

    return (
        <div className="flex-1 overflow-y-auto p-6">

            {messages.length === 0 && (
                <div className="text-center text-gray-500 mt-20">
                    Upload a document and start asking questions.
                </div>
            )}

            {messages.map((message, index) => (
                <Message
                    key={index}
                    message={message}
                />
            ))}

            {loading && <LoadingSpinner />}

        </div>
    );
}

export default ChatWindow;