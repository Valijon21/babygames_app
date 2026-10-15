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

interface Template {
  id: string;
  name: string;
  icon: string;
}

const TEMPLATES: Template[] = [
  { id: 'cat', name: 'Mushukcha', icon: '🐱' },
  { id: 'rabbit', name: 'Quyoncha', icon: '🐰' },
  { id: 'fish', name: 'Baliqcha', icon: '🐟' },
  { id: 'bear', name: 'Ayiqcha', icon: '🐻' },
  { id: 'flower', name: 'Bahoriy Gul', icon: '🌸' },
];

export const ColoringGame: React.FC<ColoringGameProps> = ({ onBack, onComplete }) => {
  const [selectedTemplate, setSelectedTemplate] = useState('cat');
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

    if (Object.keys(updated).length >= 4) {
      confetti({ particleCount: 25, spread: 50, origin: { y: 0.7 } });
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

  const handleSelectTemplate = (id: string) => {
    setSelectedTemplate(id);
    setRegionColors({});
    setHistory([{}]);
    setHistoryIndex(0);
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
          🎨 Rasm Bo‘yash
        </h2>

        <div className="flex items-center gap-1.5">
          <button
            onClick={handleUndo}
            disabled={historyIndex === 0}
            className="p-2.5 rounded-2xl bg-gray-100 text-gray-700 hover:bg-gray-200 disabled:opacity-40 min-h-[44px] min-w-[44px] flex items-center justify-center transition-all cursor-pointer"
            aria-label="Ortga qaytarish"
          >
            <Undo2 size={22} />
          </button>
          <button
            onClick={handleRedo}
            disabled={historyIndex >= history.length - 1}
            className="p-2.5 rounded-2xl bg-gray-100 text-gray-700 hover:bg-gray-200 disabled:opacity-40 min-h-[44px] min-w-[44px] flex items-center justify-center transition-all cursor-pointer"
            aria-label="Oldinga qaytarish"
          >
            <Redo2 size={22} />
          </button>
          <button
            onClick={() => setShowResetConfirm(true)}
            className="p-2.5 rounded-2xl bg-red-50 text-red-600 hover:bg-red-100 min-h-[44px] min-w-[44px] flex items-center justify-center transition-all cursor-pointer"
            aria-label="Tozalash"
          >
            <RotateCcw size={22} />
          </button>
        </div>
      </div>

      {/* Template Selector Tabs */}
      <div className="flex items-center justify-center gap-2 overflow-x-auto pb-1">
        {TEMPLATES.map((tmpl) => (
          <button
            key={tmpl.id}
            onClick={() => handleSelectTemplate(tmpl.id)}
            className={`px-4 py-2 rounded-2xl font-black text-sm flex items-center gap-2 transition-all min-h-[44px] cursor-pointer ${
              selectedTemplate === tmpl.id
                ? 'bg-pink-500 text-white shadow-md scale-105'
                : 'bg-white text-gray-700 hover:bg-pink-50 border border-pink-100'
            }`}
          >
            <span>{tmpl.icon}</span>
            <span>{tmpl.name}</span>
          </button>
        ))}
      </div>

      {/* Main Vector SVG Canvas */}
      <div className="bg-white rounded-3xl p-6 shadow-xl border-4 border-amber-200 flex flex-col items-center justify-center">
        <svg
          viewBox="0 0 400 400"
          className="w-full max-w-sm sm:max-w-md h-auto cursor-pointer drop-shadow-md select-none"
        >
          {/* Template 1: Cat */}
          {selectedTemplate === 'cat' && (
            <g>
              <circle cx="70" cy="70" r="40" fill={regionColors['sun'] || '#fef08a'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('sun')} />
              <polygon points="140,140 120,60 190,110" fill={regionColors['ear-left'] || '#ffffff'} stroke="#0f172a" strokeWidth="4" strokeLinejoin="round" onClick={() => handleRegionClick('ear-left')} />
              <polygon points="260,140 280,60 210,110" fill={regionColors['ear-right'] || '#ffffff'} stroke="#0f172a" strokeWidth="4" strokeLinejoin="round" onClick={() => handleRegionClick('ear-right')} />
              <circle cx="200" cy="180" r="80" fill={regionColors['head'] || '#ffffff'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('head')} />
              <ellipse cx="170" cy="165" rx="10" ry="14" fill="#0f172a" />
              <ellipse cx="230" cy="165" rx="10" ry="14" fill="#0f172a" />
              <circle cx="167" cy="160" r="4" fill="#ffffff" />
              <circle cx="227" cy="160" r="4" fill="#ffffff" />
              <polygon points="200,185 190,175 210,175" fill={regionColors['nose'] || '#f472b6'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('nose')} />
              <path d="M190,195 Q200,205 210,195" fill="none" stroke="#0f172a" strokeWidth="4" strokeLinecap="round" />
              <line x1="130" y1="175" x2="90" y2="165" stroke="#0f172a" strokeWidth="3" strokeLinecap="round" />
              <line x1="130" y1="185" x2="90" y2="185" stroke="#0f172a" strokeWidth="3" strokeLinecap="round" />
              <line x1="270" y1="175" x2="310" y2="165" stroke="#0f172a" strokeWidth="3" strokeLinecap="round" />
              <line x1="270" y1="185" x2="310" y2="185" stroke="#0f172a" strokeWidth="3" strokeLinecap="round" />
              <path d="M140,240 C120,290 120,350 140,360 L260,360 C280,350 280,290 260,240 Z" fill={regionColors['body'] || '#ffffff'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('body')} />
              <polygon points="180,250 220,270 220,250 180,270" fill={regionColors['bowtie'] || '#38bdf8'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('bowtie')} />
              <circle cx="200" cy="260" r="7" fill="#fbbf24" stroke="#0f172a" strokeWidth="2" />
            </g>
          )}

          {/* Template 2: Rabbit */}
          {selectedTemplate === 'rabbit' && (
            <g>
              <ellipse cx="160" cy="90" rx="20" ry="60" fill={regionColors['ear-left'] || '#ffffff'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('ear-left')} />
              <ellipse cx="160" cy="90" rx="10" ry="40" fill={regionColors['inner-left'] || '#fbcfe8'} stroke="#0f172a" strokeWidth="2" onClick={() => handleRegionClick('inner-left')} />
              <ellipse cx="240" cy="90" rx="20" ry="60" fill={regionColors['ear-right'] || '#ffffff'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('ear-right')} />
              <ellipse cx="240" cy="90" rx="10" ry="40" fill={regionColors['inner-right'] || '#fbcfe8'} stroke="#0f172a" strokeWidth="2" onClick={() => handleRegionClick('inner-right')} />
              <circle cx="200" cy="190" r="75" fill={regionColors['head'] || '#ffffff'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('head')} />
              <circle cx="175" cy="180" r="10" fill="#0f172a" />
              <circle cx="225" cy="180" r="10" fill="#0f172a" />
              <polygon points="200,200 190,192 210,192" fill={regionColors['nose'] || '#f472b6'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('nose')} />
              <path d="M190,208 Q200,218 210,208" fill="none" stroke="#0f172a" strokeWidth="3" strokeLinecap="round" />
              <ellipse cx="200" cy="300" rx="60" ry="70" fill={regionColors['body'] || '#ffffff'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('body')} />
              <ellipse cx="200" cy="305" rx="35" ry="45" fill={regionColors['belly'] || '#fef08a'} stroke="#0f172a" strokeWidth="2" onClick={() => handleRegionClick('belly')} />
            </g>
          )}

          {/* Template 3: Fish */}
          {selectedTemplate === 'fish' && (
            <g>
              <polygon points="90,200 30,140 30,260" fill={regionColors['tail'] || '#fdba74'} stroke="#0f172a" strokeWidth="4" strokeLinejoin="round" onClick={() => handleRegionClick('tail')} />
              <polygon points="200,100 240,60 270,120" fill={regionColors['topfin'] || '#fcd34d'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('topfin')} />
              <ellipse cx="220" cy="200" rx="120" ry="80" fill={regionColors['body'] || '#fed7aa'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('body')} />
              <circle cx="290" cy="180" r="12" fill="#0f172a" />
              <circle cx="286" cy="176" r="4" fill="#ffffff" />
              <path d="M320,205 Q305,215 315,225" fill="none" stroke="#0f172a" strokeWidth="4" strokeLinecap="round" />
              <ellipse cx="200" cy="225" rx="35" ry="20" fill={regionColors['sidefin'] || '#f97316'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('sidefin')} />
              <circle cx="340" cy="160" r="10" fill={regionColors['b1'] || '#e0f2fe'} stroke="#0f172a" strokeWidth="2" onClick={() => handleRegionClick('b1')} />
              <circle cx="360" cy="130" r="14" fill={regionColors['b2'] || '#e0f2fe'} stroke="#0f172a" strokeWidth="2" onClick={() => handleRegionClick('b2')} />
            </g>
          )}

          {/* Template 4: Bear */}
          {selectedTemplate === 'bear' && (
            <g>
              <circle cx="140" cy="120" r="30" fill={regionColors['ear-left'] || '#d97706'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('ear-left')} />
              <circle cx="140" cy="120" r="15" fill={regionColors['inner-left'] || '#fde68a'} stroke="#0f172a" strokeWidth="2" onClick={() => handleRegionClick('inner-left')} />
              <circle cx="260" cy="120" r="30" fill={regionColors['ear-right'] || '#d97706'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('ear-right')} />
              <circle cx="260" cy="120" r="15" fill={regionColors['inner-right'] || '#fde68a'} stroke="#0f172a" strokeWidth="2" onClick={() => handleRegionClick('inner-right')} />
              <ellipse cx="200" cy="290" rx="75" ry="85" fill={regionColors['body'] || '#b45309'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('body')} />
              <ellipse cx="200" cy="300" rx="45" ry="55" fill={regionColors['belly'] || '#fef3c7'} stroke="#0f172a" strokeWidth="2" onClick={() => handleRegionClick('belly')} />
              <circle cx="200" cy="180" r="75" fill={regionColors['head'] || '#d97706'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('head')} />
              <circle cx="175" cy="165" r="9" fill="#0f172a" />
              <circle cx="225" cy="165" r="9" fill="#0f172a" />
              <ellipse cx="200" cy="195" rx="35" ry="25" fill={regionColors['muzzle'] || '#fde68a'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('muzzle')} />
              <ellipse cx="200" cy="190" rx="14" ry="9" fill="#0f172a" />
              <path d="M192,202 Q200,210 208,202" fill="none" stroke="#0f172a" strokeWidth="3" strokeLinecap="round" />
            </g>
          )}

          {/* Template 5: Flower & Sun */}
          {selectedTemplate === 'flower' && (
            <g>
              <circle cx="80" cy="80" r="35" fill={regionColors['sun'] || '#fef08a'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('sun')} />
              <path d="M200,220 Q210,320 200,380" fill="none" stroke="#15803d" strokeWidth="12" strokeLinecap="round" />
              <ellipse cx="150" cy="310" rx="45" ry="20" transform="rotate(-30, 150, 310)" fill={regionColors['leaf-left'] || '#4ade80'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('leaf-left')} />
              <ellipse cx="250" cy="310" rx="45" ry="20" transform="rotate(30, 250, 310)" fill={regionColors['leaf-right'] || '#4ade80'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('leaf-right')} />
              {/* Petals */}
              <circle cx="200" cy="130" r="35" fill={regionColors['p1'] || '#f472b6'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('p1')} />
              <circle cx="255" cy="165" r="35" fill={regionColors['p2'] || '#f472b6'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('p2')} />
              <circle cx="240" cy="230" r="35" fill={regionColors['p3'] || '#f472b6'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('p3')} />
              <circle cx="160" cy="230" r="35" fill={regionColors['p4'] || '#f472b6'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('p4')} />
              <circle cx="145" cy="165" r="35" fill={regionColors['p5'] || '#f472b6'} stroke="#0f172a" strokeWidth="3" onClick={() => handleRegionClick('p5')} />
              {/* Flower Center */}
              <circle cx="200" cy="180" r="38" fill={regionColors['center'] || '#facc15'} stroke="#0f172a" strokeWidth="4" onClick={() => handleRegionClick('center')} />
            </g>
          )}
        </svg>
      </div>

      {/* Palette Bar */}
      <div className="bg-white rounded-3xl p-4 shadow-md border-2 border-emerald-100 flex flex-wrap items-center justify-center gap-3">
        {PALETTE.map((color) => (
          <button
            key={color}
            onClick={() => setSelectedColor(color)}
            style={{ backgroundColor: color }}
            className={`w-12 h-12 rounded-2xl border-4 transition-transform cursor-pointer ${
              selectedColor === color
                ? 'border-gray-900 scale-110 shadow-lg'
                : 'border-white shadow-xs hover:scale-105'
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
