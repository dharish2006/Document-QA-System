import SourceCard from "./SourceCard";

function Message({ message }) {
    const isUser = message.role === "user";

    return (
        <div
            className={`flex ${
                isUser ? "justify-end" : "justify-start"
            } mb-6`}
        >
            <div
                className={`max-w-4xl rounded-2xl px-5 py-4 shadow ${
                    isUser
                        ? "bg-blue-600 text-white"
                        : "bg-white"
                }`}
            >
                <p className="whitespace-pre-wrap">
                    {message.content}
                </p>

                {!isUser && (
                    <SourceCard sources={message.sources} />
                )}
            </div>
        </div>
    );
}

export default Message;