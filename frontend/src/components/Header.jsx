function Header() {
    return (
        <header className="bg-blue-600 text-white shadow">
            <div className="max-w-6xl mx-auto px-6 py-4">
                <h1 className="text-3xl font-bold">
                    Document Q&A Assistant
                </h1>

                <p className="text-blue-100 mt-1">
                    AI-powered document search using RAG and Llama 3
                </p>
            </div>
        </header>
    );
}

export default Header;