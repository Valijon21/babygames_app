import '@testing-library/jest-dom';

// Polyfill HTMLCanvasElement.prototype.getContext for JSDOM test environments
const mockContext = {
  clearRect: () => {},
  beginPath: () => {},
  moveTo: () => {},
  lineTo: () => {},
  stroke: () => {},
  fillRect: () => {},
  fillText: () => {},
  measureText: () => ({ width: 0 }),
};

// @ts-expect-error Mocking getContext for jsdom test suite
HTMLCanvasElement.prototype.getContext = () => mockContext;
