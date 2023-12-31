/*
 * This software or document includes material copied from or derived from "Sortable Table Example" 
 * https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/
 * 
 *  Copyright © 2023 World Wide Web Consortium. https://www.w3.org/copyright/software-license-2023/
 */

'use strict';

class SortableTable {
  constructor(tableNode) {
    this.tableNode = tableNode;

    this.columnHeaders = tableNode.querySelectorAll('thead th');

    this.sortColumns = [];

    for (var i = 0; i < this.columnHeaders.length; i++) {
      var ch = this.columnHeaders[i];
      var buttonNode = ch.querySelector('button.sortable');
      if (buttonNode) {
        this.sortColumns.push(i);
        buttonNode.setAttribute('data-column-index', i);
        buttonNode.addEventListener('click', this.handleClick.bind(this));
      }
    }
  }

  setColumnHeaderSort(columnIndex) {
    if (typeof columnIndex === 'string') {
      columnIndex = parseInt(columnIndex);
    }

    for (var i = 0; i < this.columnHeaders.length; i++) {
      var ch = this.columnHeaders[i];
      var buttonNode = ch.querySelector('button');
      if (i === columnIndex) {
        var value = ch.getAttribute('aria-sort');
        if (value === 'descending') {
          ch.setAttribute('aria-sort', 'ascending');
          this.sortColumn(
            columnIndex,
            'ascending',
            ch.querySelector('button.sortable-num') != null,
            ch.querySelector('button.sortable-date') != null
          );
        } else {
          ch.setAttribute('aria-sort', 'descending');
          this.sortColumn(
            columnIndex,
            'descending',
            ch.querySelector('button.sortable-num') != null,
            ch.querySelector('button.sortable-date') != null
          );
        }
      } else {
        if (ch.hasAttribute('aria-sort') && buttonNode) {
          ch.removeAttribute('aria-sort');
        }
      }
    }
  }

  sortColumn(columnIndex, sortValue, isNumber, isDate) {
    function compareValues(a,b) {
      var diff = 0

      if ((typeof b.value == "string") && (typeof a.value == "string")) {
        diff =  b.value.localeCompare(a.value);
      } else {
        diff =  a.value - b.value;
      }

      return diff * ((sortValue === 'ascending') ? 1 : -1);
    }

    if (typeof isNumber !== 'boolean') {
      isNumber = false;
    }
    if (typeof isDate !== 'boolean') {
      isDate = false;
    }

    var tbodyNode = this.tableNode.querySelector('tbody');
    var rowNodes = [];
    var dataCells = [];

    var rowNode = tbodyNode.firstElementChild;

    var index = 0;
    while (rowNode) {
      rowNodes.push(rowNode);
      var rowCells = rowNode.querySelectorAll('th, td');
      var dataCell = rowCells[columnIndex];

      var data = {};
      data.index = index;
      data.value = dataCell.textContent.trim();
      if (isNumber) {
        data.value = parseFloat(data.value);
      } else if (isDate) {
        data.value = Date.parse(data.value) || 0;
      } else if (!data.value) {
        // hack to sort based on number of childeren if no text content
        data.value = dataCell.childNodes.length
      }
      dataCells.push(data);
      rowNode = rowNode.nextElementSibling;
      index += 1;
    }

    dataCells.sort(compareValues);

    // remove rows
    while (tbodyNode.firstChild) {
      tbodyNode.removeChild(tbodyNode.lastChild);
    }

    // add sorted rows
    for (var i = 0; i < dataCells.length; i += 1) {
      tbodyNode.appendChild(rowNodes[dataCells[i].index]);
    }
  }

  /* EVENT HANDLERS */

  handleClick(event) {
    var tgt = event.currentTarget;
    this.setColumnHeaderSort(tgt.getAttribute('data-column-index'));
  }
}

// Initialize sortable table buttons
window.addEventListener('load', function () {
  var sortableTables = document.querySelectorAll('div.entry-content table');
  for (var i = 0; i < sortableTables.length; i++) {
    new SortableTable(sortableTables[i]);
  }
});
