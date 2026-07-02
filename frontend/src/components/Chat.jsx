import { useState } from "react";
import api from "../services/api";

import ChatInput from "./ChatInput";
import ChatWindow from "./ChatWindow";

function Chat() {

    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const askQuestion = async (question) => {

        setMessages(prev => [
            ...prev,
            {
                role: "user",
                content: question
            }
        ]);

        setLoading(true);

        try {

            const response = await api.post("/ask", {
                question
            });

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content: response.data.answer,
                    sources: response.data.sources
                }
            ]);

        }
        catch {

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content: "Something went wrong."
                }
            ]);

        }
        finally {

            setLoading(false);

        }

    };

    return (

        <div className="bg-white rounded-xl shadow-md h-[650px] flex flex-col">

            <div className="border-b px-6 py-4">

                <h2 className="text-2xl font-bold">
                    Conversation
                </h2>

            </div>

            <ChatWindow
                messages={messages}
                loading={loading}
            />

            <ChatInput
                onSend={askQuestion}
                loading={loading}
            />

        </div>

    );

}

export default Chat;