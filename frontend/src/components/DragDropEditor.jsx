import React from 'react';
import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';

function DragDropEditor() {
  return (
    <DndProvider backend={HTML5Backend}>
      <div className="drag-drop-editor">
        <h2>Editeur Drag & Drop</h2>
        {/* Implémenter les composants interactifs ici */}
      </div>
    </DndProvider>
  );
}

export default DragDropEditor;
