import DragDropEditor from './components/DragDropEditor';
import ApiKeyDashboard from './components/ApiKeyDashboard';

function App() {
  return (
    <div className="container">
      <h1>SaaS Low-Code</h1>
      <ApiKeyDashboard />
      <DragDropEditor />
    </div>
  );
}

export default App;
