import { Cell } from '../grid/Cell'
import { BaseModal } from './BaseModal'

type Props = {
  isOpen: boolean
  handleClose: () => void
}

export const InfoModal = ({ isOpen, handleClose }: Props) => {
  return (
    <BaseModal title="How to play" isOpen={isOpen} handleClose={handleClose}>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        Guess the Chess word or term in 6 tries. After each guess, the color of
        the tiles will change to show how close your guess was to the word.
      </p>

      <div className="flex justify-center mb-1 mt-4">
        <Cell value="S" status="correct" />
        <Cell value="P" />
        <Cell value="A" />
        <Cell value="C" />
        <Cell value="E" />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        The letter S is in the word and in the correct spot.
      </p>

      <div className="flex justify-center mb-1 mt-4">
        <Cell value="Q" />
        <Cell value="U" />
        <Cell value="E" status="present" />
        <Cell value="E" />
        <Cell value="N" />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        The letter E is in the word but in the wrong spot.
      </p>

      <div className="flex justify-center mb-1 mt-4">
        <Cell value="X" />
        <Cell value="I" />
        <Cell value="O" />
        <Cell value="N" status="absent" />
        <Cell value="G" />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        The letter N is not in the word in any spot.
      </p>

      <p className="text-sm text-gray-500 dark:text-gray-300">
        In case you need any inspriation you can have a look at the{' '}
        <a
          href="https://en.wikipedia.org/wiki/List_of_chess_grandmasters"
          className="underline font-bold"
        >
          list of grandmasters
        </a>
        , the{' '}
        <a
          href="https://en.wikipedia.org/wiki/List_of_chess_players"
          className="underline font-bold"
        >
          list of chess players
        </a>{' '}
        or the{' '}
        <a
          href="https://en.wikipedia.org/wiki/Glossary_of_chess"
          className="underline font-bold"
        >
          glossary of chess
        </a>
        .
      </p>
    </BaseModal>
  )
}
