import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/home";
import Users from "./pages/users";
import Navbar from "./components/navbar";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/users" element={<Users />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;