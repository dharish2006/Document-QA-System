import Header from "./components/Header";
import Upload from "./components/Upload";
import Chat from "./components/Chat";

function App() {
    return (
        <div className="min-h-screen bg-slate-100">

            <Header />

            <main className="max-w-6xl mx-auto py-8 px-6">

                <Upload />

                <Chat />

            </main>

        </div>
    );
}

export default App;