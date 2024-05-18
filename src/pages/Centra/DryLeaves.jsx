import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import WidgetContainer from '../../components/Cards/WidgetContainer';
import SearchLogo from '../../assets/SearchLogo.svg';
import CircularButton from '../../components/CircularButton';
import DryLeavesLogo from '../../assets/DryLeaves.svg';
import Countdown from '../../components/Countdown';
import InnerPlugins from '../../assets/InnerPlugins.svg';
import Plus from '../../assets/Plus.svg';
import CountdownIcon from  '../../assets/Countdown.svg';
import ExpiredWarningIcon from'../../assets/ExpiredWarning.svg';





function DryLeaves() {

    const data = [
        { time: "01h05m", color: "#79B2B7", image: CountdownIcon, weight: "30 Kg", code: "W232120" },
        { time: "01h45m", color: "#79B2B7", image: CountdownIcon, weight: "20 Kg", code: "W267760" },
       
      ];

      const [value, setValue] = useState("");
      const handleChange = (event, newValue) => {
        setValue(newValue);
      };

      
      

  return (
    <>
        

        <div className="mt-4  flex justify-center items-center gap-3"> 
            <WidgetContainer borderRadius="20px" className="flex items-center flex-grow">
                <div className='flex justify-start items-center gap-4'>
                <img src={SearchLogo} alt="SearchLogo" className="w-8 h-8" />
                <span className="text-green-900 text-sm font-medium leading-tight py-1 px-2 rounded font-sans">
                    Search
                </span>
                </div>
            </WidgetContainer>

            <div className='ml-1'>
                <WidgetContainer backgroundColor="#94C3B3" borderRadius="20px" border={false}>
                <img src={InnerPlugins} alt="InnerPlugins" className='w-8 h-auto ' />
                </WidgetContainer>
            </div>
        </div>

        
        {data.map((item) => (
            <div key={item.code} className=' flex justify-between'>
                <WidgetContainer borderRadius="10px" className="w-full flex items-center">
                <Link to="/dryleavesdetail">
                    <CircularButton imageUrl={DryLeavesLogo} backgroundColor="#94C3B3" />
                </Link>
                <div className='flex flex-col ml-3'>
                    <span className="font-montserrat text-base font-semibold leading-tight tracking-wide text-left">
                    {item.weight}
                    </span>
                    <span className='font-montserrat text-sm font-medium leading-17 tracking-wide text-left'>
                    {item.code}
                    </span>
                </div>
                <div className="flex ml-auto items-center">
                    <Countdown time={item.time} color={item.color} image={item.image} />
                </div>
                </WidgetContainer>
            </div>
            ))}



        <div className="flex justify-end">
            <Link to="/wetleavesdetail">
                <CircularButton imageUrl={Plus} backgroundColor="#94C3B3" />
            </Link>
        </div>


        </>     

  );
}

export default DryLeaves;
