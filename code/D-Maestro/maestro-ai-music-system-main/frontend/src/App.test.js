import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App';

test('accepts song intake and preserves the initial no-output state', () => {
  render(<App />);
  expect(screen.getByRole('heading', {name: 'Maestro AI Music Production System'})).toBeInTheDocument();
  const intake = screen.getByRole('textbox');
  fireEvent.change(intake, {target: {value: 'Southern soul with restrained drums'}});
  expect(intake).toHaveValue('Southern soul with restrained drums');
  expect(screen.getByRole('button', {name: 'Generate Music Blueprint'})).toBeInTheDocument();
  expect(screen.getByText('No blueprint generated yet.')).toBeInTheDocument();
});
