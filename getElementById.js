function getElementById(root, elementId) {
  const stack = [root];

  while (stack.length > 0) {
    const currentNode = stack.pop();

    if (currentNode.id === elementId) {
      return currentNode;
    }

    if (currentNode.children) {
      stack.push(...currentNode.children);
    }
  }

  return null;
}

// Usage
const xmlData = `
<root>
  <element id="myElementId">Some content</element>
  <element>Another element</element>
  <nested>
    <element id="nestedElementId">Nested element</element>
  </nested>
</root>
`;

const parser = new DOMParser();
const xmlDoc = parser.parseFromString(xmlData, "application/xml");
const root = xmlDoc.documentElement;
const element = getElementById(root, "myElementId");

if (element !== null) {
  console.log("Element found:", element.textContent);
} else {
  console.log("Element not found");
}




// In the JavaScript implementation, we use the DOMParser to parse the XML data and get the root element. The getElementById function takes the XML root element and the desired elementId as input.
// We use a stack to perform a depth-first search (DFS) traversal of the XML elements. Starting from the root element, we traverse through each element in the tree, checking if it has an "id" attribute matching the elementId. If a match is found, we return the element; otherwise, we continue the traversal.