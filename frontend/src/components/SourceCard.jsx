import { useState } from "react";

function SourceCard({ sources }) {
    const [open, setOpen] = useState(false);

    if (!sources || sources.length === 0) return null;

    return (
        <div className="mt-4 border rounded-xl overflow-hidden">

            <button
                onClick={() => setOpen(!open)}
                className="w-full flex justify-between items-center px-4 py-3 bg-gray-100 hover:bg-gray-200 transition"
            >
                <span className="font-medium">
                    {open ? "▼" : "▶"} Sources ({sources.length})
                </span>

                <span className="text-sm text-gray-500">
                    Click to {open ? "hide" : "show"}
                </span>
            </button>

            {open && (
                <div className="divide-y">

                    {sources.map((source, index) => (
                        <div
                            key={index}
                            className="p-4 bg-white"
                        >
                            <p className="font-semibold">
                                {source.metadata.original_filename ??
                                    source.metadata.source}
                            </p>

                            <p className="text-sm text-gray-500">
                                Chunk {source.metadata.chunk_id}
                            </p>

                            <p className="text-sm text-gray-500">
                                Similarity {(1 - source.distance).toFixed(2)}
                            </p>

                            <p className="mt-3 whitespace-pre-wrap text-gray-700">
                                {source.text}
                            </p>
                        </div>
                    ))}

                </div>
            )}

        </div>
    );
}

export default SourceCard;