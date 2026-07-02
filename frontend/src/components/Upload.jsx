import { useState } from "react";
import api from "../services/api";

function Upload() {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState("");

    const handleUpload = async () => {
        if (!file) {
            setMessage("Please select a PDF.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await api.post("/upload", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });

            setMessage(response.data.message);
        } catch (error) {
    console.log("========== ERROR ==========");
    console.log(error);
    console.log("Response:", error.response);
    console.log("Request:", error.request);
    console.log("Message:", error.message);

    setMessage(error.message);
}
    };

    return (
    <div className="bg-white rounded-xl shadow-md p-6 mb-6">

        <h2 className="text-2xl font-bold mb-5">
            Upload Document
        </h2>

        <input
            type="file"
            accept=".pdf"
            onChange={(e) => setFile(e.target.files[0])}
            className="w-full border rounded-lg p-3"
        />

        <button
            onClick={handleUpload}
            className="mt-4 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg"
        >
            Upload PDF
        </button>

        {message && (
            <div className="mt-4 text-green-700 font-medium">
                {message}
            </div>
        )}

    </div>
);
}

export default Upload;