import React, { useState } from 'react';
import { ArrowLeft, CheckCircle2, Star } from 'lucide-react';
import confetti from 'canvas-confetti';
import { Button } from '../../components/ui/Button';

interface NumbersGameProps {
  onBack: () => void;
  onComplete: (score: number) => void;
}

interface Question {
  id: number;
  prompt: string;
  emoji: string;
  count: number;
  options: number[];
  answer: number;
}

const QUESTIONS: Question[] = [
  { id: 1, prompt: 'Nechta quvnoq olma bor?', emoji: '🍎', count: 3, options: [2, 3, 4], answer: 3 },
  { id: 2, prompt: 'Yulduzchalarni sanang:', emoji: '⭐', count: 5, options: [4, 5, 6], answer: 5 },
  { id: 3, prompt: 'Qushchalarni toping:', emoji: '🐥', count: 2, options: [1, 2, 3], answer: 2 },
  { id: 4, prompt: 'Mazali sabzilar nechta?', emoji: '🥕', count: 6, options: [5, 6, 7], answer: 6 },
  { id: 5, prompt: 'Chiroyli gullarni sanang:', emoji: '🌸', count: 4, options: [3, 4, 5], answer: 4 },
];

export const NumbersGame: React.FC<NumbersGameProps> = ({ onBack, onComplete }) => {
  const [currentIdx, setCurrentIdx] = useState(0);
  const [score, setScore] = useState(0);
  const [countedItems, setCountedItems] = useState<number[]>([]);
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null);

  const q = QUESTIONS[currentIdx];

  const handleTapItem = (index: number) => {
    if (!countedItems.includes(index)) {
      setCountedItems([...countedItems, index]);
    }
  };

  const handleSelectOption = (num: number) => {
    if (num === q.answer) {
      confetti({ particleCount: 40, spread: 60, origin: { y: 0.7 } });
      setFeedback('correct');
      setScore(score + 1);

      setTimeout(() => {
        setFeedback(null);
        setCountedItems([]);
        if (currentIdx < QUESTIONS.length - 1) {
          setCurrentIdx(currentIdx + 1);
        } else {
          onComplete(10);
        }
      }, 1200);
    } else {
      setFeedback('wrong');
      setTimeout(() => setFeedback(null), 1000);
    }
  };

  return (
    <div className="max-w-3xl mx-auto p-4 flex flex-col gap-5">
      {/* Top Bar */}
      <div className="flex items-center justify-between bg-white rounded-3xl p-4 shadow-md border-2 border-emerald-100">
        <Button variant="outline" size="md" onClick={onBack} className="gap-2">
          <ArrowLeft size={22} />
          <span>Orqaga</span>
        </Button>

        <h2 className="text-xl sm:text-2xl font-black text-gray-800">
          🔢 1 dan 10 gacha sanash
        </h2>

        <div className="flex items-center gap-1.5 bg-amber-100 text-amber-900 px-4 py-2 rounded-2xl font-bold">
          <Star size={20} className="fill-amber-500 text-amber-500" />
          <span>{score} ball</span>
        </div>
      </div>

      {/* Main Question Board */}
      <div className="bg-white rounded-3xl p-8 shadow-xl border-4 border-emerald-200 flex flex-col items-center justify-center text-center">
        <span className="text-sm font-bold text-emerald-600 uppercase tracking-wider mb-2">
          Savol {currentIdx + 1} / {QUESTIONS.length}
        </span>
        <h3 className="text-2xl sm:text-3xl font-black text-gray-800 mb-6">
          {q.prompt}
        </h3>

        {/* Clickable counting items */}
        <div className="flex flex-wrap items-center justify-center gap-4 max-w-lg mb-8 min-h-[120px]">
          {Array.from({ length: q.count }).map((_, i) => (
            <button
              key={i}
              onClick={() => handleTapItem(i)}
              className={`text-6xl sm:text-7xl p-3 rounded-2xl transition-all cursor-pointer transform active:scale-90 ${
                countedItems.includes(i)
                  ? 'bg-amber-100 ring-4 ring-amber-400 scale-110 shadow-lg'
                  : 'hover:scale-105'
              }`}
            >
              {q.emoji}
              {countedItems.includes(i) && (
                <span className="block text-xs font-black text-amber-800 mt-1">
                  {countedItems.indexOf(i) + 1}
                </span>
              )}
            </button>
          ))}
        </div>

        {/* Options */}
        <div className="flex flex-wrap gap-4 justify-center">
          {q.options.map((opt) => (
            <button
              key={opt}
              onClick={() => handleSelectOption(opt)}
              className="w-20 h-20 rounded-3xl bg-blue-500 hover:bg-blue-600 text-white font-black text-3xl shadow-lg hover:shadow-xl active:scale-95 transition-all flex items-center justify-center cursor-pointer"
            >
              {opt}
            </button>
          ))}
        </div>

        {/* Feedback message */}
        {feedback === 'correct' && (
          <div className="mt-6 flex items-center gap-2 text-emerald-600 font-black text-2xl animate-bounce">
            <CheckCircle2 size={32} />
            <span>To‘g‘ri! Barakalla! 🎉</span>
          </div>
        )}
        {feedback === 'wrong' && (
          <div className="mt-6 text-pink-500 font-bold text-xl animate-pulse">
            Qaytadan sanab ko‘ring! 😊
          </div>
        )}
      </div>
    </div>
  );
};
