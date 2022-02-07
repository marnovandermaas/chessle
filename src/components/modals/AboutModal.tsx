import { BaseModal } from './BaseModal'

type Props = {
  isOpen: boolean
  handleClose: () => void
}

export const AboutModal = ({ isOpen, handleClose }: Props) => {
  return (
    <BaseModal title="About" isOpen={isOpen} handleClose={handleClose}>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        This is a Chess-themed version of Wordle{' '}
        <a
          href="https://github.com/marnovandermaas/chessle"
          className="underline font-bold"
        >
          check out the code here
        </a>.{' '}
        It is inspired by{' '}
        <a
          href="https://www.powerlanguage.co.uk/wordle/"
          className="underline font-bold"
        >
          the original Wordle
        </a>{' '}
        and the bike-themed version{' '}
        <a
          href="https://github.com/giop98/bikle"
          className="underline font-bold"
        >
          Bikle
        </a>.{' '}
        The code is based on{' '}
        <a
          href="https://github.com/cwackerfuss/react-wordle"
          className="underline font-bold"
        >
          Reactle
        </a>.{' '}
      </p>
    </BaseModal>
  )
}
