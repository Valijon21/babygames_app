import React, { useState } from 'react';
import { Undo2, Redo2, RotateCcw, ArrowLeft, CheckCircle2 } from 'lucide-react';
import confetti from 'canvas-confetti';
import { Button } from '../../components/ui/Button';

interface ColoringGameProps {
  onBack: () => void;
  onComplete: (score: number) => void;
}

const PALETTE = [
  '#ef4444', // Red
  '#f97316', // Orange
  '#facc15', // Yellow
  '#22c55e', // Green
  '#06b6d4', // Cyan
  '#3b82f6', // Blue
  '#8b5cf6', // Purple
  '#ec4899', // Pink
  '#854d0e', // Brown
  '#ffffff', // White
];

export const ColoringGame: React.FC<ColoringGameProps> = ({ onBack, onComplete }) => {
  const [selectedColor, setSelectedColor] = useState(PALETTE[0]);
  const [regionColors, setRegionColors] = useState<Record<string, string>>({});
  const [history, setHistory] = useState<Array<Record<string, string>>>([{}]);
  const [historyIndex, setHistoryIndex] = useState(0);
  const [showResetConfirm, setShowResetConfirm] = useState(false);

  const handleRegionClick = (regionId: string) => {
    const updated = { ...regionColors, [regionId]: selectedColor };
    const newHistory = history.slice(0, historyIndex + 1);
    newHistory.push(updated);
    setHistory(newHistory);
    setHistoryIndex(newHistory.length - 1);
    setRegionColors(updated);

    // If most regions are colored, trigger celebratory confetti
    if (Object.keys(updated).length >= 5) {
      confetti({ particleCount: 30, spread: 60, origin: { y: 0.7 } });
    }
  };

  const handleUndo = () => {
    if (historyIndex > 0) {
      const prev = history[historyIndex - 1];
      setHistoryIndex(historyIndex - 1);
      setRegionColors(prev);
    }
  };

  const handleRedo = () => {
    if (historyIndex < history.length - 1) {
      const next = history[historyIndex + 1];
      setHistoryIndex(historyIndex + 1);
      setRegionColors(next);
    }
  };

  const handleReset = () => {
    setRegionColors({});
    setHistory([{}]);
    setHistoryIndex(0);
    setShowResetConfirm(false);
  };

  const handleFinish = () => {
    confetti({ particleCount: 100, spread: 80, origin: { y: 0.6 } });
    onComplete(10);
  };

  return (
    <div className="max-w-4xl mx-auto p-4 flex flex-col gap-4">
      {/* Top Bar */}
      <div className="flex items-center justify-between bg-white rounded-3xl p-4 shadow-md border-2 border-emerald-100">
        <Button variant="outline" size="md" onClick={onBack} className="gap-2">
          <ArrowLeft size={22} />
          <span>Orqaga</span>
        </Button>

        <h2 className="text-xl sm:text-2xl font-black text-gray-800">
          🎨 Quvnoq Mushukcha
        </h2>

        <div className="flex items-center gap-1.5">
          <button
            onClick={handleUndo}
            disabled={historyIndex === 0}
            className="p-2.5 rounded-2xl bg-gray-100 text-gray-700 hover:bg-gray-200 disabled:opacity-40 min-h-[44px] min-w-[44px] flex items-center justify-center transition-all"
            aria-label="Ortga qaytarish"
          >
            <Undo2 size={22} />
          </button>
          <button
            onClick={handleRedo}
            disabled={historyIndex >= history.length - 1}
            className="p-2.5 rounded-2xl bg-gray-100 text-gray-700 hover:bg-gray-200 disabled:opacity-40 min-h-[44px] min-w-[44px] flex items-center justify-center transition-all"
            aria-label="Oldinga qaytarish"
          >
            <Redo2 size={22} />
          </button>
          <button
            onClick={() => setShowResetConfirm(true)}
            className="p-2.5 rounded-2xl bg-red-50 text-red-600 hover:bg-red-100 min-h-[44px] min-w-[44px] flex items-center justify-center transition-all"
            aria-label="Tozalash"
          >
            <RotateCcw size={22} />
          </button>
        </div>
      </div>

      {/* Main Canvas & Drawing Area */}
      <div className="bg-white rounded-3xl p-6 shadow-xl border-4 border-amber-200 flex flex-col items-center justify-center">
        <svg
          viewBox="0 0 400 400"
          className="w-full max-w-sm sm:max-w-md h-auto cursor-pointer drop-shadow-md select-none"
        >
          {/* Background Sun */}
          <circle
            cx="70"
            cy="70"
            r="40"
            fill={regionColors['sun'] || '#fef08a'}
            stroke="#0f172a"
            strokeWidth="4"
            onClick={() => handleRegionClick('sun')}
          />
          {/* Cat Ears */}
          <polygon
            points="140,140 120,60 190,110"
            fill={regionColors['ear-left'] || '#ffffff'}
            stroke="#0f172a"
            strokeWidth="4"
            strokeLinejoin="round"
            onClick={() => handleRegionClick('ear-left')}
          />
          <polygon
            points="260,140 280,60 210,110"
            fill={regionColors['ear-right'] || '#ffffff'}
            stroke="#0f172a"
            strokeWidth="4"
            strokeLinejoin="round"
            onClick={() => handleRegionClick('ear-right')}
          />
          {/* Cat Head */}
          <circle
            cx="200"
            cy="180"
            r="80"
            fill={regionColors['head'] || '#ffffff'}
            stroke="#0f172a"
            strokeWidth="4"
            onClick={() => handleRegionClick('head')}
          />
          {/* Cat Eyes */}
          <ellipse cx="170" cy="165" rx="10" ry="14" fill="#0f172a" />
          <ellipse cx="230" cy="165" rx="10" ry="14" fill="#0f172a" />
          <circle cx="167" cy="160" r="4" fill="#ffffff" />
          <circle cx="227" cy="160" r="4" fill="#ffffff" />
          {/* Cat Nose */}
          <polygon
            points="200,185 190,175 210,175"
            fill={regionColors['nose'] || '#f472b6'}
            stroke="#0f172a"
            strokeWidth="3"
            onClick={() => handleRegionClick('nose')}
          />
          {/* Cat Mouth & Whiskers */}
          <path d="M190,195 Q200,205 210,195" fill="none" stroke="#0f172a" strokeWidth="4" strokeLinecap="round" />
          <line x1="130" y1="175" x2="90" y2="165" stroke="#0f172a" strokeWidth="3" strokeLinecap="round" />
          <line x1="130" y1="185" x2="90" y2="185" stroke="#0f172a" strokeWidth="3" strokeLinecap="round" />
          <line x1="270" y1="175" x2="310" y2="165" stroke="#0f172a" strokeWidth="3" strokeLinecap="round" />
          <line x1="270" y1="185" x2="310" y2="185" stroke="#0f172a" strokeWidth="3" strokeLinecap="round" />
          {/* Cat Body */}
          <path
            d="M140,240 C120,290 120,350 140,360 L260,360 C280,350 280,290 260,240 Z"
            fill={regionColors['body'] || '#ffffff'}
            stroke="#0f172a"
            strokeWidth="4"
            onClick={() => handleRegionClick('body')}
          />
          {/* Cat Bowtie */}
          <polygon
            points="180,250 220,270 220,250 180,270"
            fill={regionColors['bowtie'] || '#38bdf8'}
            stroke="#0f172a"
            strokeWidth="3"
            onClick={() => handleRegionClick('bowtie')}
          />
          <circle cx="200" cy="260" r="7" fill="#fbbf24" stroke="#0f172a" strokeWidth="2" />
        </svg>
      </div>

      {/* Color Palette Selector */}
      <div className="bg-white rounded-3xl p-4 shadow-md border-2 border-emerald-100 flex flex-wrap items-center justify-center gap-3">
        {PALETTE.map((color) => (
          <button
            key={color}
            onClick={() => setSelectedColor(color)}
            style={{ backgroundColor: color }}
            className={`w-12 h-12 rounded-2xl border-4 transition-transform ${
              selectedColor === color
                ? 'border-gray-900 scale-110 shadow-lg'
                : 'border-white shadow-sm hover:scale-105'
            }`}
            aria-label={`Rang: ${color}`}
          />
        ))}
      </div>

      {/* Action Finish Button */}
      <div className="flex justify-center">
        <Button variant="secondary" size="lg" onClick={handleFinish} className="gap-2">
          <CheckCircle2 size={26} />
          <span>Tayyor bo‘ldi!</span>
        </Button>
      </div>

      {/* Reset Confirmation Dialog */}
      {showResetConfirm && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/40 backdrop-blur-xs">
          <div className="bg-white rounded-3xl p-6 max-w-sm w-full shadow-2xl text-center flex flex-col gap-4">
            <h3 className="text-xl font-black text-gray-800">
              Rasmni tozalaymizmi?
            </h3>
            <p className="text-sm text-gray-600">
              Barcha bo‘yalgan ranglar boshlang‘ich holatiga qaytadi.
            </p>
            <div className="flex gap-3 justify-center">
              <Button variant="outline" size="md" onClick={() => setShowResetConfirm(false)}>
                Yo‘q
              </Button>
              <Button variant="secondary" size="md" onClick={handleReset}>
                Ha, tozalash
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
