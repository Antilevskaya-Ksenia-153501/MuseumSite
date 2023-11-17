let tableData = [];
let selectedCells = [];
  function generateTable() {
      let sizeInput = document.getElementById('size');
      let size = parseInt(sizeInput.value);
      if (isNaN(size)){
          alert('Enter correct size of table');
          return;
      }
      if (size <= 0){
          alert('Size of table must be greater than zero');
          return;
      }

      let table = document.getElementById('squareTable');
      table.innerHTML = '';

      tableData = [];
      selectedCells = [];

      for (let i = 0; i < size; i++){
          let row = [];
          let tr = document.createElement('tr');
          table.appendChild(tr);
      
          for (let i=0; i < size; i++){
              let cellValue = Math.floor(Math.random() * 100) + 1;
              row.push(cellValue);

              let td = document.createElement('td');
              td.textContent = cellValue;
              td.onclick = cellClickHandler;
              tr.appendChild(td);
          }
          tableData.push(row);
      }
  }  

  function transposeTable() {
    if (tableData.length !== tableData[0].length) {
        alert('The number of rows is not equal to the number of columns!');
    }
    else {
        let table = document.getElementById('squareTable');
        let rows = table.rows;

        let transposedData = [];
        for (let i = 0; i < rows.length; i++) {
            let rowData = [];
            for (let j = 0; j < rows[i].cells.length; j++) {
              rowData.push(tableData[j][i]);
            }
            transposedData.push(rowData);
        }

        table.innerHTML = '';
        tableData = transposedData;

        for (let i = 0; i < tableData.length; i++) {
            let tr = document.createElement('tr');
            table.appendChild(tr);

            for (let j = 0; j < tableData[i].length; j++) {
              var td = document.createElement('td');
              td.textContent = tableData[i][j];
              td.onclick = cellClickHandler;
              tr.appendChild(td);
            }
        }
    }
  }

  function addRow() {
      let table = document.getElementById('squareTable');
      let newRow = [];
      let tr = document.createElement('tr');
      table.appendChild(tr);

      for (let i = 0; i < tableData[0].length; i++){
          let cellValue = Math.floor(Math.random() * 100) + 1;
          newRow.push(cellValue);
          let td = document.createElement('td');
          td.textContent = cellValue;
          td.onclick = cellClickHandler;
          tr.appendChild(td);
      }
      tableData.push(newRow);
  }

  function addColumn() {
      let table = document.getElementById('squareTable');
      let rows = table.rows;

      for (let i = 0; i < rows.length; i++) {
          let cellValue = Math.floor(Math.random() * 100) + 1;
          tableData[i].push(cellValue);

          let td = document.createElement('td');
          td.textContent = cellValue;
          td.onclick = cellClickHandler;
          rows[i].appendChild(td);
      }
  }

  function cellClickHandler() {
      let maxSelectedInput = document.getElementById('maxSelected');
      let maxSelectionPerRow = parseInt(maxSelectedInput.value);
      if (isNaN(maxSelectionPerRow)){
        alert('Enter correct size of table');
        return;
      }
      if (maxSelectionPerRow <= 0){
        alert('Size of table must be greater than zero');
        return;
      }
      let cell = this;
      let value = parseInt(cell.textContent);
      let row = cell.parentNode;

      let selectedCellsInRow = Array.from(row.cells).filter(selectedCell =>
          selectedCells.includes(selectedCell)
      );

      if (selectedCellsInRow.length < maxSelectionPerRow && !isNeighborSelected(cell, selectedCellsInRow)) {
          cell.style.backgroundColor = value % 2 === 0 ? 'lightblue' : 'lightgreen';
          selectedCells.push(cell);
      } else if (selectedCells.includes(cell)) {
          cell.style.backgroundColor = '';
          selectedCells = selectedCells.filter(selectedCell => selectedCell !== cell);
      }
  }

function isNeighborSelected(cell, selectedCellsInRow) {
    let cellIndex = Array.from(cell.parentNode.cells).indexOf(cell);

    if (cellIndex > 0) {
        let leftCell = cell.parentNode.cells[cellIndex - 1];
        if (selectedCellsInRow.includes(leftCell)) {
            return true;
        }
    }

    if (cellIndex < cell.parentNode.cells.length - 1) {
        let rightCell = cell.parentNode.cells[cellIndex + 1];
        if (selectedCellsInRow.includes(rightCell)) {
            return true;
        }
    }
    return false;
}