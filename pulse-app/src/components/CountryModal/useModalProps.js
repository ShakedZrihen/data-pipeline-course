import { useState } from "react";

const useModalProps = () => {
  const [open, setOpen] = useState(true);

  return { open, openModal: () => setOpen(true), onClose: () => setOpen(false) };
};

export default useModalProps;
