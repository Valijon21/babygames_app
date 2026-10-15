import React, { useState } from 'react';
import { ShieldCheck, Check, AlertCircle } from 'lucide-react';
import { Modal } from '../../components/ui/Modal';
import { Button } from '../../components/ui/Button';

interface ParentGateModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSuccess: () => void;
}

export const ParentGateModal: React.FC<ParentGateModalProps> = ({
  isOpen,
  onClose,
  onSuccess,
}) => {
  const [num1] = useState(Math.floor(Math.random() * 8) + 7); // 7 to 14
  const [num2] = useState(Math.floor(Math.random() * 8) + 5); // 5 to 12
  const [inputAnswer, setInputAnswer] = useState('');
  const [error, setError] = useState(false);

  const correctAnswer = num1 + num2;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (parseInt(inputAnswer.trim(), 10) === correctAnswer) {
      setError(false);
      setInputAnswer('');
      onSuccess();
    } else {
      setError(true);
    }
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Ota-onalar nazorati">
      <form onSubmit={handleSubmit} className="flex flex-col gap-4 text-center">
        <div className="w-16 h-16 rounded-full bg-purple-100 text-purple-600 flex items-center justify-center mx-auto">
          <ShieldCheck size={32} />
        </div>

        <p className="text-sm text-gray-600">
          Ushbu bo‘limga faqat kattalar kirishi mumkin. Davom etish uchun quyidagi misolni yeching:
        </p>

        <div className="bg-purple-50 p-4 rounded-2xl border-2 border-purple-200 text-2xl font-black text-purple-900 tracking-wider">
          {num1} + {num2} = ?
        </div>

        <input
          type="number"
          value={inputAnswer}
          onChange={(e) => {
            setInputAnswer(e.target.value);
            setError(false);
          }}
          placeholder="Javobni kiriting..."
          className="w-full text-center text-xl font-bold p-3 rounded-2xl border-2 border-gray-300 focus:border-purple-500 focus:ring-4 focus:ring-purple-100 outline-none"
          autoFocus
        />

        {error && (
          <div className="flex items-center justify-center gap-1.5 text-red-500 text-sm font-bold">
            <AlertCircle size={16} />
            <span>Javob noto‘g‘ri. Qayta urinib ko‘ring.</span>
          </div>
        )}

        <div className="flex gap-3 justify-end mt-2">
          <Button variant="outline" size="md" type="button" onClick={onClose}>
            Bekor qilish
          </Button>
          <Button variant="primary" size="md" type="submit" className="gap-2 bg-purple-600 hover:bg-purple-700">
            <Check size={20} />
            <span>Tasdiqlash</span>
          </Button>
        </div>
      </form>
    </Modal>
  );
};
