import { useState } from "react";

const useModalProps = () => {
  const [open, setOpen] = useState(false);
  const [props, setProps] = useState({});

  return {
    ...props,
    open,
    openModal: (props) => {
      setProps(props);
      setOpen(true);
    },
    onClose: () => setOpen(false)
  };
};

export default useModalProps;
