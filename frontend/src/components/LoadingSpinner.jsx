function LoadingSpinner() {
    return (
        <div className="flex items-center gap-3 py-4">
            <div className="w-4 h-4 rounded-full bg-blue-500 animate-bounce"></div>
            <div className="w-4 h-4 rounded-full bg-blue-500 animate-bounce delay-150"></div>
            <div className="w-4 h-4 rounded-full bg-blue-500 animate-bounce delay-300"></div>

            <span className="text-gray-600">
                Thinking...
            </span>
        </div>
    );
}

export default LoadingSpinner;