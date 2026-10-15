import React, { useState, useRef, useEffect } from 'react';
import { ArrowLeft, Volume2, RefreshCw, CheckCircle } from 'lucide-react';
import confetti from 'canvas-confetti';
import { Button } from '../../components/ui/Button';

interface AlphabetGameProps {
  onBack: () => void;
  onComplete: (score: number) => void;
}

const UZBEK_LETTERS = [
  { char: 'A', lower: 'a', word: 'Anor', emoji: '🍎' },
  { char: 'B', lower: 'b', word: 'Baliq', emoji: '🐟' },
  { char: 'D', lower: 'd', word: 'Daraxt', emoji: '🌳' },
  { char: 'E', lower: 'e', word: 'Eshik', emoji: '🚪' },
  { char: 'F', lower: 'f', word: 'Fil', emoji: '🐘' },
  { char: 'G', lower: 'g', word: 'Gul', emoji: '🌸' },
  { char: 'H', lower: 'h', word: 'Humo', emoji: '🕊️' },
  { char: 'I', lower: 'i', word: 'It', emoji: '🐶' },
  { char: 'J', lower: 'j', word: 'Jo‘ja', emoji: '🐥' },
  { char: 'K', lower: 'k', word: 'Kitob', emoji: '📖' },
  { char: 'L', lower: 'l', word: 'Lola', emoji: '🌷' },
  { char: 'M', lower: 'm', word: 'Mushuk', emoji: '🐱' },
  { char: 'N', lower: 'n', word: 'Non', emoji: '🍞' },
  { char: 'O', lower: 'o', word: 'Olma', emoji: '🍏' },
  { char: 'P', lower: 'p', word: 'Pichoq', emoji: '🔪' },
  { char: 'Q', lower: 'q', word: 'Quyosh', emoji: '☀️' },
  { char: 'R', lower: 'r', word: 'Rasm', emoji: '🎨' },
  { char: 'S', lower: 's', word: 'Sabzi', emoji: '🥕' },
  { char: 'T', lower: 't', word: 'Toshbaqa', emoji: '🐢' },
  { char: 'U', lower: 'u', word: 'Uzum', emoji: '🍇' },
  { char: 'V', lower: 'v', word: 'Velosiped', emoji: '🚲' },
  { char: 'X', lower: 'x', word: 'Xurmo', emoji: '🌴' },
  { char: 'Y', lower: 'y', word: 'Yulduz', emoji: '⭐' },
  { char: 'Z', lower: 'z', word: 'Zebra', emoji: '🦓' },
  { char: 'O‘', lower: 'o‘', word: 'O‘rdak', emoji: '🦆' },
  { char: 'G‘', lower: 'g‘', word: 'G‘oz', emoji: '🪿' },
  { char: 'Sh', lower: 'sh', word: 'Shar', emoji: '🎈' },
  { char: 'Ch', lower: 'ch', word: 'Choynak', emoji: '🫖' },
  { char: 'Ng', lower: 'ng', word: 'Tong', emoji: '🌅' },
];

export const AlphabetGame: React.FC<AlphabetGameProps> = ({ onBack, onComplete }) => {
  const [selectedIdx, setSelectedIdx] = useState(0);
  const current = UZBEK_LETTERS[selectedIdx];
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [hasDrawn, setHasDrawn] = useState(false);

  // Play audio phonetics synthesis
  const playSound = (text: string) => {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 0.85;
      utterance.pitch = 1.1;
      window.speechSynthesis.speak(utterance);
    }
  };

  // Clear tracing canvas
  const clearCanvas = () => {
    const canvas = canvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext('2d');
      if (ctx) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    }
    setHasDrawn(false);
  };

  // Drawing event handlers for touch and mouse
  const startDrawing = (e: React.MouseEvent | React.TouchEvent) => {
    setIsDrawing(true);
    setHasDrawn(true);
    draw(e);
  };

  const stopDrawing = () => {
    setIsDrawing(false);
    const canvas = canvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext('2d');
      ctx?.beginPath();
    }
  };

  const draw = (e: React.MouseEvent | React.TouchEvent) => {
    if (!isDrawing) return;
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const rect = canvas.getBoundingClientRect();
    let clientX = 0;
    let clientY = 0;

    if ('touches' in e) {
      clientX = e.touches[0].clientX;
      clientY = e.touches[0].clientY;
    } else {
      clientX = e.clientX;
      clientY = e.clientY;
    }

    const x = clientX - rect.left;
    const y = clientY - rect.top;

    ctx.lineWidth = 14;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.strokeStyle = '#3b82f6';

    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
  };

  const handleSelectLetter = (idx: number) => {
    setSelectedIdx(idx);
    clearCanvas();
    playSound(UZBEK_LETTERS[idx].char);
  };

  const handleFinishTracing = () => {
    confetti({ particleCount: 50, spread: 70, origin: { y: 0.6 } });
    if (selectedIdx < UZBEK_LETTERS.length - 1) {
      setSelectedIdx(selectedIdx + 1);
      clearCanvas();
    } else {
      onComplete(10);
    }
  };

  useEffect(() => {
    clearCanvas();
  }, [selectedIdx]);

  return (
    <div className="max-w-5xl mx-auto p-4 flex flex-col gap-5">
      {/* Top Header */}
      <div className="flex items-center justify-between bg-white rounded-3xl p-4 shadow-md border-2 border-emerald-100">
        <Button variant="outline" size="md" onClick={onBack} className="gap-2">
          <ArrowLeft size={22} />
          <span>Orqaga</span>
        </Button>

        <h2 className="text-xl sm:text-2xl font-black text-gray-800">
          🔤 O‘zbek Alifbosi
        </h2>

        <Button
          variant="secondary"
          size="md"
          onClick={() => playSound(`${current.char}. ${current.word}`)}
          className="gap-2"
        >
          <Volume2 size={22} />
          <span className="hidden sm:inline">Eshitish</span>
        </Button>
      </div>

      {/* Main Focus: Letter Card + Tracing Pad */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
        {/* Letter Card */}
        <div className="bg-gradient-to-br from-blue-50 to-indigo-100 rounded-3xl p-8 shadow-xl border-4 border-blue-200 flex flex-col items-center justify-center text-center">
          <div className="text-7xl sm:text-9xl font-black text-blue-600 drop-shadow-sm select-none">
            {current.char} {current.lower}
          </div>
          <div className="mt-4 text-5xl sm:text-6xl">{current.emoji}</div>
          <div className="mt-2 text-3xl font-black text-gray-800">{current.word}</div>
          <button
            onClick={() => playSound(current.char)}
            className="mt-5 px-6 py-3 rounded-2xl bg-blue-500 hover:bg-blue-600 text-white font-bold flex items-center gap-2 shadow-md active:scale-95 transition-all"
          >
            <Volume2 size={24} />
            <span>Talaffuz: {current.char}</span>
          </button>
        </div>

        {/* Tracing Area */}
        <div className="bg-white rounded-3xl p-6 shadow-xl border-4 border-amber-200 flex flex-col items-center justify-between relative">
          <div className="w-full flex items-center justify-between mb-2">
            <span className="font-bold text-gray-700">✍️ Harf izidan yozish</span>
            <button
              onClick={clearCanvas}
              className="px-3 py-1.5 rounded-xl bg-gray-100 hover:bg-gray-200 text-gray-600 text-sm font-bold flex items-center gap-1.5 transition-all"
            >
              <RefreshCw size={16} />
              <span>Tozalash</span>
            </button>
          </div>

          {/* Canvas with background guideline */}
          <div className="relative w-full aspect-square max-w-[320px] rounded-2xl border-2 border-dashed border-gray-300 bg-gray-50 flex items-center justify-center overflow-hidden">
            <span className="absolute text-9xl font-black text-gray-200 select-none pointer-events-none">
              {current.char}
            </span>
            <canvas
              ref={canvasRef}
              width={320}
              height={320}
              className="absolute inset-0 cursor-crosshair touch-none"
              onMouseDown={startDrawing}
              onMouseUp={stopDrawing}
              onMouseMove={draw}
              onTouchStart={startDrawing}
              onTouchEnd={stopDrawing}
              onTouchMove={draw}
            />
          </div>

          <div className="w-full flex justify-between gap-3 mt-4">
            <Button
              variant="outline"
              size="md"
              onClick={() => setSelectedIdx((prev) => (prev > 0 ? prev - 1 : prev))}
              disabled={selectedIdx === 0}
            >
              Oldingi
            </Button>
            <Button
              variant="accent"
              size="md"
              onClick={handleFinishTracing}
              className="gap-2"
            >
              <CheckCircle size={20} />
              <span>{hasDrawn ? 'Barakalla!' : 'Keyingisi'}</span>
            </Button>
          </div>
        </div>
      </div>

      {/* Alphabet Grid Selector */}
      <div className="bg-white rounded-3xl p-4 shadow-md border-2 border-emerald-100">
        <h3 className="text-base font-bold text-gray-700 mb-3 px-2">Barcha harflar:</h3>
        <div className="grid grid-cols-5 sm:grid-cols-10 gap-2">
          {UZBEK_LETTERS.map((item, idx) => (
            <button
              key={item.char}
              onClick={() => handleSelectLetter(idx)}
              className={`p-2 rounded-2xl font-black text-lg transition-all min-h-[48px] min-w-[48px] flex items-center justify-center ${
                selectedIdx === idx
                  ? 'bg-blue-500 text-white shadow-lg scale-110'
                  : 'bg-blue-50 text-blue-800 hover:bg-blue-100'
              }`}
            >
              {item.char}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};
